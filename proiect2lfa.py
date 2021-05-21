def nfa_dfa1(multime):
    global a, dfa_nrstari
    next={}
    dfa_nrstari.append(multime) 
    for i in multime:
        for j in range(len(a)):
            for m in a[i][j]:
                if m in next:
                    if j not in next[m]:
                        next[m].append(j)
                else:
                    next[m]=[j]
    nfa_dfa2(next, multime)

def nfa_dfa2(dictionar, multime):
    global stari_finale, dfa_stari_fin, dfa_nr_tranzitii
    for i,j in dictionar.items():
        print(multime, j, i)
        dfa_nr_tranzitii+=1
        for b in j:
            if (b in stari_finale) and (j not in dfa_stari_fin) :
                dfa_stari_fin.append(j)
                break
        if j not  in dfa_nrstari:
            nfa_dfa1(j)



cin=open("fisier.txt")
alf = set()
nr_stari,nr_tranzitii = tuple(map(int,cin.readline().split())) #numarul total de stari, numarul total de tranzitii
a = [[[] for h in range(nr_stari)] for i in range(nr_stari)] 
while nr_tranzitii:
    nr_tranzitii -= 1
    i,j, lit = cin.readline().split()
    alf.add(lit)
    a[int(i)][int(j)].append(lit)
stare_initiala = int(cin.readline()) #stare initiala
stari_finale = list(map(int,cin.readline().split())) [1:] #prima pozitie = nr stari finale, dupa avem starile finale
print(a)
dfa_nrstari=[]
dfa_stari_fin=[]
dfa_nr_tranzitii=0

def dfa():
    global dfa_nrstari, dfa_stari_fin, stare_initiala, stari_finale, dfa_nr_tranzitii
    if stare_initiala in stari_finale:
        dfa_stari_fin.append(stare_initiala)
    nfa_dfa1([stare_initiala])
    print("Numar de stari DFA: ", len(dfa_nrstari))
    print("Starile sunt: ", dfa_nrstari)
    print("Starea initiala este: ", [stare_initiala])
    print("Starile finale sunt: ", dfa_stari_fin)
    print("Numar de tranzitii DFA: ", dfa_nr_tranzitii)

dfa()
cin.close()