from sys import argv 
script,filename=argv
txt = open(filename)
print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again =input("> ")
txt_again = open(file_again,'w')
#0000print (txt_again.read())
print("Truncatind the file.")
txt_again.truncate()
print("now write the lines")
line1=input(">")
line2=input(">")
txt_again.write(line1)

txt_again.write("\n")
txt_again.write(line2)
print("And finally ,we close it")
txt_again.close()
