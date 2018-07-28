def print_none():
    print "hello world."
def print_one(arg):
    print"I like %r."%arg
def print_two(arg1,arg2):
    print"I like %r and %r."%(arg1,arg2)
print_none()
print_one("apple")
print_two("apple","banana")
##########
def add(a,b):
    return a+b
A=20
B=30
total=add(A,B)
print"Total is %d."%total
####################
def w(x,y):
    return (x+y,x-y,x*y,x/y,x//y,x%y,-x,+x,abs(x),int(x),float(x),complex(x,y),divmod(x,y),pow(x,y),x**y)   
print w(2,3) 
#################
a=(1,2,3)
#a[1]=8 no 
print a[1]
b=[4,5,6]
b[0]=0
print b[0]
#############
c=range(3)
print c
#############
d="apple"
print d[0],d[1]
d='apple'
print d[0],d[1]
#a[2]='b' wrong
#################
things="apple orange banana grape pear"
stuff1=things.split(' ')
stuff2=things.split(',')
print''.join(stuff1)
print','.join(stuff1)
print''.join(stuff2)
print','.join(stuff2)
##############
x="appa"
print x in stuff2
print x not in stuff2
print x+str(stuff1)
print 5*str(stuff1)
e=range(5)
print e[2:4]
print e[0:4:2]
print len(str(stuff2))
print x.index('a')
print x.count('a')
##################################################
s=['appl','lexy']
s[0]='x'
print s
