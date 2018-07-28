###from sys import argv
###script,textfile=argv
####textfile=raw_input()
from sys import argv
script,first,textfile=argv

#text=open(textfile)
#print"the content of %s:"%textfile
#print text.read()

text=open(textfile,'w')
line1="Myname is purple monster."
line2="I am 34."
line3="I like teaching."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()

text=open(textfile,"r+")
new=open(first,"w+")
new.write(text.read())
text.close()
new.close()
