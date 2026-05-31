text = 'Robin,Zajicek           '
encoding = text.encode('utf-8') 
print(encoding)

print(text[0])
print(text[:0])
print(text[0:])

print(text.upper())
print(text.lower())
print(text.find('Z'))
print(text.strip())

print('Do variables')
name,last_name = text.split(',')
print(name)
print(last_name)
