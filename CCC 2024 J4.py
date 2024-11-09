right = input() + "."
wrong = input() + "."

if len(right) == len(wrong):
    quietkey = '-'
    key = list(set(right) - set(wrong))
    wrongkey = list(set(wrong)-set(right))[0]
    print(key[0], wrongkey)
    print(quietkey)
else:
    wrongkey = list(set(wrong) - set(right))[0]
    key = set(right) - set(wrong)
    count = 0
    while count < len(wrong):
        while right[count] == wrong[count]:
            count +=1
        if wrong[count] != wrongkey:
            quietkey = right[count]
            break
        else:
            count +=1
    print(*(key-set(quietkey)), wrongkey)
    print(quietkey)
