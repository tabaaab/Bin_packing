import os
import matplotlib.pyplot as plt
import numpy as np
import itertools




def fichier_csv(list1):
    #list1=lecteur_metoile(dataset)
    with open('firstfitdat3.csv', 'w') as f:
        for item in list1:
            f.write("%s\n" %item)


def desin(liste,liste2,liste3,liste4,liste5):
    ls = []
    ls = lecteur_metoile(dataset)
    #premier algo best fit
    plt.subplot(321)
    plt.plot(liste,"r-", label="solution heuristique")
    plt.plot(ls,"k-", label="optimal")
    plt.grid(True)
    plt.title(' (Best fit) ')
    #deuxiéme algo next fit
    plt.subplot(322)
    plt.plot(liste2, "y-", label="solution heuristique")
    plt.plot(ls, "k-", label="optimal")
    plt.grid(True)
    plt.title('(Next fit)')
    # troisieme algo next fit decreasing
    plt.subplot(323)
    plt.plot(liste3, "c-", label="solution heuristique")
    plt.plot(ls, "k-", label="optimal")
    plt.grid(True)
    plt.title('(Next fit decreasing)')
    #4éme algo first fit 
    plt.subplot(324)
    plt.plot(liste4, "g-", label="solution des heuristics")
    plt.plot(ls, "k-", label="optimal")
    plt.grid(True)
    plt.title('(first fit )')
    plt.legend()
    plt.suptitle('comparaison entre les solution réalisable des algorithmes heuristics et les sol optimal', fontsize=20)
    #5éme algo first fit dec
    plt.subplot(325)
    plt.plot(liste5, "m-", label="solution des heuristics")
    plt.plot(ls, "k-", label="optimal")
    plt.grid(True)
    plt.title('(first fit decreasing )')
    plt.legend()
    plt.show()


def explorer_arbores(dataset):

    path = r'C:\Users\abdel\PycharmProjects\pythonProject1'
    slash="\\"
    chemin=path+slash+dataset
    nom = []
    files = os.listdir(chemin)
    for name in files:
        nom.append(name)
    return nom


def lecteur_metoile(dataset):
    if dataset == "bin1data":
        fichier="metoile1.txt"
    if dataset=="bin2data":
        fichier="metoile2.txt"
    if dataset=="bin3data":
        fichier="metoile3.txt"

    nvx=[]
    planetes = open(fichier, 'r')
    lignes = planetes.readlines()
    planetes.close()
    tab = []
    for chn in lignes:
        tab.append(chn.split(','))
    merged = list(itertools.chain(*tab))
    merged = [x.replace('\t', ',').replace('\n', ',') for x in merged]
    merged2 = [s.split(',') for s in merged]
    merged2 = list(itertools.chain(*merged2))
    nvx = [x for x in merged2 if x]
    for i in range(0, len(nvx)):
        nvx[i] = int(nvx[i])
    return nvx

def lecture_fichier(fichier):
    with open(fichier, 'r') as filehandle:
        # pour mon fichier
        list_of_lists = []
        for line in filehandle:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)
    filehandle.close()
    merged = list(itertools.chain(*list_of_lists))
    for i in range(0, len(merged)):
        merged[i] = int(merged[i])
    return (merged)


def sol(dataset):
    ls = explorer_arbores(dataset)
    v=lecteur_metoile(dataset)
    my = []
    final1=[]
    final2=[]
    final3=[]
    final4=[]
    final5=[]
    path = r'C:\Users\abdel\PycharmProjects\pythonProject1'
    slash = "\\"
    for i in range(len(ls)):
        name = path + slash + dataset+ slash +ls[i]
        my = lecture_fichier(name)
        nv=[my[i] for i in range(2,len(my))]
        final1.append(best_fit(my[1], nv))
        final2.append(next_fit(my[1], nv))
        final3.append(next_fit_dec(my[1], nv))
        final4.append(first_fit(my[1], nv))
        final5.append(first_fit_dec(my[1], nv))

    solution=desin(final1,final2,final3,final4,final5)
    fichier_csv(final4)

    return solution


def best_fit(c, w):
    n=len(w)
    if n == 0:
        return 0

    Bins = [c]
    for i in range(len(w)):
        RC = []
        RCind = []
        for j in range(len(Bins)):
            if w[i] <= Bins[j]:
                RC.append(Bins[j] - w[i])
                RCind.append(j)
        if len(RC) > 0:
            Bins[RCind[np.argmin(RC)]] -= w[i]
        else:
            Bins.append(c)
            Bins[len(Bins)-1] -= w[i]

    return len(Bins)

def next_fit(c, w):
    n=len(w)
    if n == 0:
        return 0

    curBin = c
    nBins = 1
    for i in range(len(w)):
        if w[i] <= curBin:
            curBin -= w[i]
        else:
            curBin = c-w[i]
            nBins += 1
    return nBins


def next_fit_dec(c, w):
    n=len(w)
    if n == 0:
        return 0

    wSorted = sorted(w, reverse = True)
    return next_fit(c, wSorted)

def first_fit(c, w):
    n=len(w)
    if n == 0:
        return 0
    Bins = [c]
    for i in range(len(w)):
        nFit = False
        for j in range(len(Bins)):
            if w[i] <= Bins[j]:
                Bins[j] = Bins[j] - w[i]
                break
            if j == len(Bins)-1:
                nFit = True
        if nFit is True:
            Bins.append(c)
            Bins[len(Bins)-1] -= w[i]

    return len(Bins)


def first_fit_dec(c, w):
    n=len(w)
    if n == 0:
        return 0
    wSorted = w.copy()
    wSorted.sort(reverse = True)
    return first_fit(c, wSorted)



dataset="bin3data"

#w = lecture_fichier()
#n=len(w)
#c = 100
#print("Number of bins required in Next Fit :",next_fit(n,c,w))
#print("les instances sont : ",explorer_arbores())
sol(dataset)

#print(lecteur_metoile())



