# data= {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# with open('file.txt','w') as file:
#     file.write("dictionary_name = { \n")
#     for k in sorted (data.keys()):
#         file.write("'%s':'%s', \n" % (k, data[k]))
#     file.write("}")

# with open('file.txt', 'w+') as file:
#     file.write(str(data))

details = {'Name': "Alice",
           'Age': 21,
           'Degree': "Bachelor Cse",
           'University': "Northeastern Univ"}

with open("myfile.json", 'w') as f:
    for key, value in details.items():
        f.write('%s:%s\n' % (key, value))

f = open("myfile.json", "r")  #Oku
print(f.read())