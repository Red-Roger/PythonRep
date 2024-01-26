import pika
from models_rabbit import Contacts
import connect

import faker


def main():
    
    fake_data = faker.Faker()
    
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    
    for _ in range(5):
        fn = fake_data.name()
        em = fake_data.email()
        tl = fake_data.phone_number()
        isem = fake_data.boolean()
        Contacts (fullname = fn, email = em, phone = tl, isemail = isem,  issent = False).save()
        cont = Contacts.objects(fullname = fn).first()
        email_id = cont.id
    
        if isem == True:
            channel.queue_declare(queue='emails')
            channel.basic_publish(exchange='', routing_key='emails', body=f'{email_id}'.encode())
        else:
            channel.queue_declare(queue='phones')
            channel.basic_publish(exchange='', routing_key='phones', body=f'{email_id}'.encode())
        
        print(f" [x] Sent {email_id}")
        cont = Contacts.objects(id = email_id)
        cont.update (issent = True)
    
    connection.close()
    

if __name__ == '__main__':
    main()