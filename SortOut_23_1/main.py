from multiprocessing import Process, freeze_support

result_list = []

def calculate (number):
    list = []
    for i in range (number):
        if number%(i+1) == 0:
            list.append(i+1)
    result_list.append(list)

def factorize(*number):

    for n in number:
        w = Process(target=calculate (n))
        freeze_support()
        w.start()

    return result_list

if __name__ == '__main__':
    freeze_support()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)


