file = open ('newFile.pdf', 'w')
content = "Hello World, this is amazing\n"

file.write(content.upper())

#Reading a file
#file = open('newFile.pdf', 'r')
#data = file.read()
#print(data)

#Appending content to a file
#file = open('newFile.pdf', 'a')
#file.write("Invite JsMammie to the party\n")

#Error handling with try-except
try:
    file = open('newFile.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
   print("File not found")