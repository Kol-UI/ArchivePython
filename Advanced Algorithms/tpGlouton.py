def tpGlouton(equipe1,equipe2,tot1,tot2,liste,ind):
    print(ind,tot1,tot2)
    if ind==len(liste):
        return equipe1,equipe2
    else:
        if tot1<=tot2:
            tot1+=liste[ind]
            equipe1.append(liste[ind])
        else:
            tot2+=liste[ind]
            equipe2.append(liste[ind])
        return tpGlouton(equipe1,equipe2,tot1,tot2,liste,ind+1)


liste=[13,4,1,7,2,9,10,20]
liste=sorted(liste, reverse=True)
print(tpGlouton([],[],0,0,liste,0))
