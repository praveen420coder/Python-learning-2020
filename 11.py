from sys import argv
script,file=argv
def print_all(f):
 print(f.read())
 
def rewind(f):
 f.seek(0)
 
def print_a_line(line_count,f):
 print(line_count,f.readline())
 
current_file=open(file)
print("let's print the whole file.")
print_all(current_file)
print("now let's rewind like tape.")
rewind(current_file)
print("let's print three lines")
line1=1
print_a_line(line1,current_file)
line1=line1+1
print_a_line(line1,current_file)