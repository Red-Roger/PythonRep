def encode(data):
    res = []

    def recur (new_data):
        key = False
        if len(new_data) > 1:
            count = 0
            first = new_data [0]
            c = 1
            for value in new_data:
                if value == first:
                    count += 1
                else:
                    res.append(first)
                    res.append(count)
                    ind = new_data.index(value)
                    new_data = new_data [ind:]
                    break
                m = len (new_data)
                if c == m:
                    res.append(first)
                    res.append(count)
                    key = True
                c += 1
            if key == False:               
                recur(new_data)
    recur(data)
    return res


data3 = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]

print (encode(data3))