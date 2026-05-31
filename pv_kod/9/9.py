#Integrita dat, bezpečnost, logování, kontrola vstupů, zpracování chyb

#spravny datovy typ, pravidla
#validace stringu - regex
#try, except,finaly, asserts 
x = int(input('zadej cislo'))
try:
    vysledek = 10/x
    print('dobre mrdko')
except ZeroDivisionError as err:
    err('ses pica')
    
#loggovani zkus tu knihovnu .env sql inj ,xss ,csfr,debugiing