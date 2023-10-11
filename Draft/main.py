def make_request(keys, values):
    res_vocab = {}
    if len(keys) != len (values):
        return res_vocab
    else:
        for k_value in keys:
            res_vocab[k_value] = values[keys.index(k_value)]
    return res_vocab
       
keys = ["name", "fname", "rates"]
values = ["wiki", "pedia", [1, 4, 5, 6]]
print (make_request (keys, values))