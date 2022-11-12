def logistic_encrypt(plain_text: str, r: float) -> str:
    assert 3.6 < r < 4.0
    asc = []
    for c in plain_text:
        asc.append(ord(c))
    for i in range(len(asc)):
        if asc[i] == 10:
            asc[i] = 1
        else:
            asc[i] -= 30
    x = float("0." + str(len(asc)))

    def logistic(r, x):
        return r * x * (1 - x)

    maplist = []
    indexlist = []
    for i in range(len(asc)):
        x = logistic(r, x)
    for i in range(96):
        x = logistic(r, x)
        while x in maplist:
            x = logistic(r, x)
        maplist.append(x)
        indexlist.append(x)

    indexlist.sort(key=float)
    cipherlist = []
    for i in range(len(asc)):
        element = maplist.index(indexlist[asc[i] - 1])
        cipherlist.append(element)
    for i in range(len(asc)):
        if cipherlist[i] == 0:
            cipherlist[i] = 10
        else:
            cipherlist[i] += 31
    cipher_text = ''.join(map(chr, cipherlist))
    return cipher_text


def logistic_decrypt(cipher_text: str, r: float) -> str:
    assert 3.6 < r < 4.0
    asc = []
    for c in cipher_text:
        if ord(c) == 10:
            asc.append(1)
        else:
            asc.append(ord(c) - 30)
    num = "0." + str(len(asc))
    x = float(num)

    def logistic(r, x):
        return r * x * (1 - x)

    maplist = []
    indexlist = []
    for i in range(len(asc)):
        x = logistic(r, x)
    for i in range(96):
        x = logistic(r, x)
        while (x in maplist):
            x = logistic(r, x)
        maplist.append(x)
        indexlist.append(x)
    indexlist.sort(key=float)
    decryptlist = []
    for i in range(len(asc)):
        element = indexlist.index(maplist[asc[i] - 1])
        decryptlist.append(element)
    for i in range(len(decryptlist)):
        if decryptlist[i] == 0:
            decryptlist[i] = 10
        else:
            decryptlist[i] += 31
    decrypted_text = ''.join(map(chr, decryptlist))
    return decrypted_text
