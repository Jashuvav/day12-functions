while True:
    def cal():
        a=int(input("a: "))
        b=int(input("b: "))
        option=int(input('''choosee options 1.add 2.sub 3.mul'''))
        if option == 1:
            print(a+b)
        elif option == 2:
            print(a-b)
        elif option == 3:
            print(a*b)
        else:
            print("invalid input")
            break
        cal()


def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a: "))
    b=int(input("b: "))
    option=int(input('''choosee options 1.add 2.sub 3.mul'''))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()

def splitbill():
    a=int(input("frinds: "))
    b=int(input("amount: "))
    print("bill is ",b//a)
splitbill()


def splitbill():
    a=int(input("frinds: "))
    b=int(input("amount: "))
    print(f"bill is :{b//a}")
splitbill()



#keywords and positionaal argunments
'''def details(id,name,mail):
    id=10
    name="jashuva"
    mail="j@gmail.com"
    print(id,name,mail)
details(id="id",name="name",mail="mail")'''

def details(id,name,mail):
    print(id,name,mail)
details(id="id",name="name",mail="mail")
details(id=20,name="joe",mail="h@gmail.com")
details(29,jash,h@.coom)
details(j@.com,44,kow)
details(mail="hj@.com",id=34,name="nooo")


#default argument
def grocery(item,price):
    print("item is %s:"%item)
    print("item is %d:"%price)
grocery("sugar",100)

def grocery(item="rice",price=2000):
    print("item is %s:"%item)
    print("item is %d:"%price)
grocery()

def grocery(item,price=2500):
    print("item is %s:"%item)
    print("item is %d:"%price)
grocery("dhal")

def grocery(item="tamata",price):
    #non def arg follows def arg
    print("item is %s:"%item)
    print("item is %d:"%price)
grocery(100)



def bakery(cake,price,qty):
    print("cake is %s:"%cake)
    print("prince is %d:"%price)
    print("qty is %d:"%qty)
bakery("coco",2000,3)
