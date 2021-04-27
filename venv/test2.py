def firstfit():
    taille = len(objet)
    res = 0
    liste = [10] * taille
    j = 0

    for j in range(len(res)):
        if liste[j] >= objet[i]:
            liste[j] = liste[j] - objet[i]

        if j == res:
            liste[res] = c - liste[j]
            res = res + 1

    return res


objet = [3, 4, 4, 3, 3, 2, 1]
c = 10

print("nombre des boites : ", nextfit(objet, c))