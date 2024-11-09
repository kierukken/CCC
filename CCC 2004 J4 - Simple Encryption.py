letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
keydict = [letters.find(i) for i in list(input())]
input = [letters.find(i) if i.isalpha() else None for i in list(input())]

counter = 0
keydictcounter = 0
while counter < len(input):
    try:
        while input[counter] == None:
            del input[counter]
        input[counter] = (input[counter] + keydict[keydictcounter])%26
        keydictcounter += 1
        counter += 1
        if keydictcounter == len(keydict):
            keydictcounter = 0
    except IndexError:
        break
print(''.join([letters[i] for i in input]))
