#Algoritmizace - Rekurze, Brute Force, Heuristiky, Nedeterministické algoritmy

#Rekurze 
#funkce vola sama sebe - nejkratsi cesta prohledavani stromu 
# prima = vola sama sebe
# neprima = a na c pak na b pak na a 
# faktoril and fin
pole = [1,1,2,3,5,8,13,21,34]

def fin(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    return fin(value - 1) + fin(value -2)
print(fin(12))

#deter - presne definovan krok, spravny vysledek na vztupu (Brute Force - hesla) 
#nedeter - jiny vysledek +- vysledky(Monte Carlo - lodicky) #MonteCarlo je heuristicky alg
