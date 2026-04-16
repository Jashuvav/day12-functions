#* arguments -> * is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)
print(type(a))

a=(2,3,4,5,6,7,8)
print(a)
print(*a)
print(type(a))

a={2,3,4,5,6,7,8}
print(a)
print(*a)
print(type(a))

a={"year":2004,"name":"jashi"}
print(a)
print(*a)
print(type(a))


a="jashuva"
print(*a)
print(type(a))

a,b,c=3,5,7
print(a)
print(b)
print(c)

a,b,c=2,4,5,6,7,7,8
print(a)
print(b)
print(c) #value error

a,b,*c=2,4,5,6,7,7,8
print(a)
print(b)
print(*c)

a,*b,c=2,4,5,6,7,7,8
print(a)
print(*b)
print(c)


a,b,c="jashuva"
print(a)
print(b)
print(c) #value error

a,b,c="jas"
print(a)
print(b)
print(c)

a,*b,c="jashuva"
print(a)
print(*b)
print(c)

*a,b,c="jashuva"
print(*a)
print(b)
print(c)

#variable length argunments -> these are automatically store in tuple we use * argunments

def check(*a):
    print(a)
    print(tuple(a))
check()
check(2,3,4,5,6,7)
b=[3,4,5,6,7,8,9]
check(*b)
c=(4,5,6,7,8)
check(*c)
d={3,4,5,6,7,8}
check(*d)
e={"name":"jashuva","year":2020}
check(*e)'''

def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(a) in (int,float):
                      d=d+i
                      print(d)
check1()
check1(3,4,5,6,7,8,8)
check1(3,4.4,5.5,4,5)
check1(3,6.6,3,7,"jashu")


#kwargs(**) -> it gives distinoary as result
def check(**a):
    print(a)
    print(type(a))
check()
d={"ids":[10,20,30],
   "names":["jahs","hoe","devi"],
   "status":["p","a","p"]}
check(**d)

def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
d={"ids":[10,20,30],
   "names":["jahs","hoe","devi"],
   "status":["p","a","p"]}
check(**d)



#*,** -> useage
def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("valuse is",j)
final()
data=(3,4,5,6.5,4.5)
final(*data)
details={"ids":[10,20,30],
   "names":["jahs","hoe","devi"],
   "status":["p","a","p"]}
final(**details)
final(*data,**details)


#min(),#max(), #sum()
print(max(3,4,5,6,67,4,2))
print(min(3,2,4,5,7,8))
a=[2,3,4,5]
print(sum(a))
