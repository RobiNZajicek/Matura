import re 


pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|web|cz)'
while True:
    try:
        email = input('Prosim zadejte email:')
        if not re.search(pattern,email):
            raise(ValueError)
        print("Spravne")
        break
    except ValueError:
        print("spatny mail")
#       
text = 'dasdasdas dasdsadasd           '

#encoding
