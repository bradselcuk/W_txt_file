file = ['Name: ','LastName: ','Phone: ']

with open('dosya.txt', 'w') as f: # Yaz
    for x in file:
        f.write("%s\n" % x)
# ---------------------------------------
f = open("dosya.txt", "r")  #Oku
print(f.read())

