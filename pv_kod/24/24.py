text = int(input('zadej cislo'))

def vypocitaniDeleni(a,b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError as e:
        e('Nemuzes delit 0 :)')
        
vypocitaniDeleni(5,text)

#Dale muzeme delat skromny test assertem

