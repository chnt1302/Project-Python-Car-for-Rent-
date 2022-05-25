import os
os.system ('cls')
import sqlite3
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

print('='*160)
txt = ("🚗  WELCOME TO CAR FOR RENT 🚗".center(165))
print(txt)
txt22 = ("-----  กรอกข้อมูลเพื่อติดตามรถ  -----")
x22 = txt22.center(170)
print(x22)
print('='*160)
cost = []
st = {}

def login():
    global y
    print('\t    ''1. เข้าสู่ระบบ'.center(155))
    print('\t    ''2. สมัครสมาชิก'.center(155))
    print('\t              ''***** กรุณาสมัครสมากชิกก่อนเเข้าใช้งาน (กรณียังไม่ได้สมัครสมากชิก) *****'.center(155))
    y = input('โปรดเลือกคำตอบของคุณ : ')

def newuser():
    global Createuser,Createpass
    Createuser = input("Create Username = ")
    Createpass = input("Create Password = ")
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('''INSERT INTO Register (username,password) VALUES (?,?)''',(Createuser,Createpass))
    conn.commit()
    conn.close()
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('''SELECT username,password FROM Register''')
    result = c.fetchall()
    for x in result:
        i = 0
        while i <= len(result):
            if Createuser and Createpass not in x:
                print(Fore.LIGHTWHITE_EX + Back.GREEN + "\n\t\t\t\t\t\t\t\t   +++++ สมัครสมาชิกเรียบร้อย +++++")
                olduser()
            else:
                break
        if Createuser and Createpass in x:
            print("ชื่อผู้ใช้นี้มีอยู่แล้ว")
            newuser()
        i+=1
    conn.commit()

       
def olduser():
    print("\n\t\t\t\t\t\t\t\t\t    [ L O G I N ]\n")
    Loging = input("\t\t\t\t\t\t\t\t\t    ID = ")
    Password = input("\t\t\t\t\t\t\t\t\t  Password = ")
    conn = sqlite3.connect (r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('''SELECT username,password FROM Register''') #สามารถ login ได้อีกครั้ง หากสมัครสมาชิกแล้ว
    conn.commit ()
    result = c.fetchall()
    for x in result:
        i = 0
        while i <= len(result):
            if Loging and Password in x:
                print(Fore.LIGHTWHITE_EX + Back.GREEN + "\n\t\t\t\t\t\t\t\t   +++++ เข้าสู่ระบบเรียบร้อย +++++")
                customerinfo()
            else:
                break
    if Loging and Password not in x:
        print(Fore.LIGHTWHITE_EX + Back.RED + "\n\t\t\t\t\t\t\t\t   +++++ ชื่อผู้ใช้ หรือ รหัสผ่าน ไม่ถูกต้อง +++++")
        olduser()
    conn.close ()

def checking(): #เพิ่มข้อจำกัดตัวเลขให้พอดีกับข้อมูล
        global personalid
        personalid = input('เลขบัตรประชาชน : ')
        for i in range(1):
            if len(personalid) !=13:
                print(Fore.LIGHTWHITE_EX + Back.RED + 'โปรดใส่จำนวนเลขบัตรให้ครบ 13 หลัก')
                checking()
            elif personalid.isdigit() == False:
                    print(Fore.LIGHTWHITE_EX + Back.RED + 'โปรดใส่จำนวนเลขบัตรให้ครบ 13 หลัก')
                    checking()

def checking2():#เพิ่มข้อจำกัดตัวเลขและตัวอักษรให้กับข้อมูล
        global tel
        tel = input('เบอร์โทรศัพท์ : ')
        for i in range(1):
            if len(tel) !=9:
                if len(tel) !=10:
                    print(Fore.LIGHTWHITE_EX + Back.RED +'โปรดใส่จำนวนเบอร์โทรศัพท์ให้ครบ 9 หรือ 10 หลัก')
                    checking2()
                elif tel.isdigit() == False:
                    print(Fore.LIGHTWHITE_EX + Back.RED +'โปรดใส่จำนวนเบอร์โทรศัพท์ให้ครบ 9 หรือ 10 หลัก')
                    checking2()
            elif tel.isdigit() == False:
                    print(Fore.LIGHTWHITE_EX + Back.RED +'โปรดใส่จำนวนเบอร์โทรศัพท์ให้ครบ 9 หรือ 10 หลัก')
                    checking2()       

def customerinfo(): #เพิ่มข้อมูลที่ผู้ใช้ต้องกรอก
    global fname,lname,personalid,address,job,nationality,tel,email,a,y,info
    print('='*175)
    print("กรุณากรอกข้อมูลด้วยครับ/ค่ะ")
    fname = input('\nชื่อจริง : ')
    lname = input('นามสกุลจริง : ')
    checking()
    address = input('ที่อยู่ : ')
    job = input('อาชีพ : ')
    nationality = input('สัญชาติ : ')
    checking2()
    email = input('อีเมล : ')
    #เก็บข้อมูลผู้ใช้เป็นตัวแปร dict เพื่อสำหรับการแก้ไชและอัพเดตข้อมูล
    info = {'fname':fname,'lname':lname,'personalid':personalid,'address':address,'job':job,'nationality':nationality,'tel':tel,'email':email}
    os.system('cls')
    print('='*155)
    print('ข้อมูลผู้เช่า'.center(155))
    print('='*155)
    print('\t\t\t\t\t\t\t\t  ',fname,lname,'\n\t\t\t\t\t\tที่อยู่ :',address,'\n\t\t\t\t\t\t\tอาชีพ :',job,'\t\tสัญชาติ :',nationality,'\n\t\t\t\t\tเลขบัตรประชาชน :',personalid,'\t\tเบอร์โทรศัพท์ :',tel,'\n\t\t\t\t\t\t\tอีเมล :',email)
    def edit():
        global a,xx,newfname,newlname
        conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
        c = conn.cursor()
        c.execute('''INSERT INTO customerinfo (fname,lname,personalid,address,job,nationality,tel,email) VALUES (?,?,?,?,?,?,?,?)''',(info['fname'],info['lname'],info['personalid'],info['address'],info['job'],info['nationality'],info['tel'],info['email']))
        conn.commit()
        conn.close
        print('='*155)
        print('หากต้องการแก้ไขข้อมูล กด [0]')
        print('แสดงข้อมูลที่แก้ไข กด [s]') 
        print('หากไม่ต้องการแก้ไขข้อมูล กด [9]')
        a = input('กรุณาเลือกทำรายการ : ')
        print('-'*155)
        if a == '0': #เพิ่มส่วนของ การแก้ไขข้อมูล
            print('ชื่อจริง กด [1]'.center(155))   
            print('นามสกุลจริง กด [2]'.center(155))  
            print('เลขบัตรประชาชน กด [3]'.center(155))  
            print('ที่อยู่ กด [4]'.center(155))  
            print('อาชีพ กด [5]'.center(155))  
            print('สัญชาติ กด [6]'.center(155)) 
            print('เบอร์โทรศัพท์ กด [7]'.center(155)) 
            print('อีเมล กด [8]'.center(155))
            xx = input('กรุณาเลือกทำรายการ : ') 
            print('-'*155)
            if xx == '1':
                newfname = input('แก้ไขข้อมูลเป็น : ')
                info.update({'fname':newfname})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['fname'] + ' เรียบร้อย')
                edit()
            elif xx == '2':
                newlname = input('แก้ไขข้อมูลเป็น : ')
                info.update({'lname':newlname})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['lname'] + ' เรียบร้อย')
                edit()
            elif xx == '3':
                newpersonalid = input('แก้ไขข้อมูลเป็น : ')
                info.update({'personalid':newpersonalid})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['personalid'] + ' เรียบร้อย')
                edit()
            elif xx == '4':
                newaddress = input('แก้ไขข้อมูลเป็น : ')
                info.update({'address':newaddress})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['address'] + ' เรียบร้อย')
                edit()
            elif xx == '5':
                newjob = input('แก้ไขข้อมูลเป็น : ')
                info.update({'job':newjob})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['job'] + ' เรียบร้อย')
                edit()
            elif xx == '6':
                newnationality = input('แก้ไขข้อมูลเป็น : ')
                info.update({'nationality':newnationality})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['nationality'] + ' เรียบร้อย')
                edit()
            elif xx == '7':
                newtel = input('แก้ไขข้อมูลเป็น : ')
                info.update({'tel':newtel})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['tel'] + ' เรียบร้อย')
                edit()
            elif xx == '8':
                newemail = input('แก้ไขข้อมูลเป็น : ')
                info.update({'email':newemail})
                print(Fore.LIGHTWHITE_EX + Back.GREEN + 'แก้ไขข้อมูลเป็น ' + info['email'] + ' เรียบร้อย')
                edit()
            else:
                print(Fore.LIGHTWHITE_EX + Back.RED +'ระบบผิดพลาด')
                edit()
        elif a == '9':
            choosekindofcar()
        elif a == 's': #ตรงนี้จะแสดงข้อมูลผู้ใช้หลังจากการแก้ไข
            print('='*155)
            print('ข้อมูลผู้เช่า'.center(155))
            print('='*155)
            print('\t\t\t\t\t\t\t\t  ',info['fname'],info['lname'],'\n\t\t\t\t\t\tที่อยู่ :',info['address'],'\n\t\t\t\t\t\t\tอาชีพ :',info['job'],'\t\tสัญชาติ :',info['nationality'],'\n\t\t\t\t\tเลขบัตรประชาชน :',info['personalid'],'\t\tเบอร์โทรศัพท์ :',info['tel'],'\n\t\t\t\t\t\t\tอีเมล :',info['email'])
            print('='*155)
            edit()
        else:
            print(Fore.LIGHTWHITE_EX + Back.RED +'ระบบผิดพลาด กรุณาทำรายการอีกครั้ง')
            edit()
    edit()
    print('-'*155)

def choosekindofcar ():
    os.system('cls')
    print('TYPE OF CAR'.center(160))
    import car
    car.car1
    car.car2
    car.car3
    car.car4
    
    global choice
    print('\t\t\t\tโปรดเลือกประเภทรถ\n \t\t\t\t1.SUPER CAR\n \t\t\t\t2.SEDAN\n \t\t\t\t3.PICKUP TRUCK \n \t\t\t\t4.MORTORCYCLE\n')
    choice = input('\t\t\t\t\t\t\t\tYOUR ANSWER : ')
    if choice == '1':
        supercar()
        exit()
        login()
    elif choice == '2':
        sedan()
        exit()
        login()
    elif choice == '3':
        pickuptruck()
        exit()
        login()
    elif choice == '4':
        motorcycle()
        exit()
        login()
    else:
        choosekindofcar()

def supercar():
    import car
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Carinfo WHERE Typeofcar = "SUPER CAR"')
    result = c.fetchall()
    conn.commit()
    print('='*175)
    o=0
    for x in result:
        o+=1
        print("\n\t\t\t\t          ",o,x[1] +'       ', x[4],'In Stock ', x[5])
    print('='*175)
    price = [0,80000 , 48000 , 75000 , 85000]
    h1 = "+++++ หากไม่คืนตามนัดจะมีความผิดตามกฏหมาย +++++"
    z = int(input('โปรดเลือกรถของคุณ : '))
    namecar = [0,'Lamborghini Aventador','Lamborghini Huracan','Ferrari 488 GTB','Ferrari 812 GTS']
    st = {z:namecar[z]} #ทำการเก็บชื่อรถไว้ในตัวแปร dict ใช้สำหรับค้นหาชื่อใน database เพื่อทำ stock
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    cc = c.execute(f"""SELECT instock FROM Carinfo where nameofcar ="{st[z]}" """) #ค้นหาชื่อรถจาก databae ตามที่ได้เลือก
    result = cc.fetchall()
    for i in result:  # i บรรทัดนี้เมื่อ print แล้วจะออกมาเป็นข้อมูลประเภท tuple
        x = list(i)  #ทำการ cast เพื่อแปลง tuple ให้เป็น list
        y = int(x[0])  #ทำการ print ค่าใน list ออกมาแล้ว cast เป็นตัวแปร int เพื่อใช้ในการลบ 
    s=y-1
    if s >-1:
        a = (s,st[z])
        c=conn.cursor()
        c.execute('''UPDATE Carinfo set instock = ? WHERE nameofcar = ?''',a)
        conn.commit()
        c.close()
        y = int(input('จำนวนวันที่ต้องการเช่า : ')) 
        cost.append(price[z])
        for a in cost:
            total = a*y
        print('ราคาที่ต้องชำระ คือ ',total)
        print("="*152)
        def Bill():
            c = conn.cursor()
            c.execute('''INSERT INTO rentalhistory (fname,lname,personalid,Tel,address,job,nationality,email,car,day,cost) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(info['fname'],info['lname'],info['personalid'],info['tel'],info['address'],info['job'],info['nationality'],info['email'],namecar[z],y,total))
            conn.commit()
            print(Fore.LIGHTYELLOW_EX + '='*152)
            x = '🚗  ใบเสร็จ 🚗'
            txt=x.center(152)
            print(txt)
            print(Fore.LIGHTYELLOW_EX + '='*152)
            print("\n")
            name ="                                                              [ {}  {} ]                                                                 "
            print(name.format(info['fname'] ,info['lname']))
            print("\n") 
            id ="                                                                  [ {} ]                                                                   "
            print(id.format(info['personalid']))
            print("\n")
            add ="                                                   [ {} ]                                                                   "
            print(add.format(info['address']))
            print("\n")
            phone ="                                                   [ {} ]  [ {} ]                                                                 "
            print(phone.format(info['tel'],info['email']))
            print("\n")
            print(Fore.LIGHTYELLOW_EX + '-'*152)
            n1 ="                                                     {}                                                                                   "
            print(n1.format(car.car1))
            n ="                                                             [ {} ]                                                                                    "
            print(n.format(namecar[z]))
            print('\n')
            b ="จำนวนวันที่เช่า   {}   วัน     ราคา   {}   บาท".center(152)
            print(b.format(y,total))
            print("\n")
            h ="                                                     {}                                                                "
            print(h.format(h1))
            print("\n")
            print('# # # # # THANK YOU # # # # #'.center(152))
            print(Fore.LIGHTYELLOW_EX + '='*152)
        def bill1():
            bill = input('พิมพ์ใบเสร็จ กด [b] : ')
            if bill == 'b':
                os.system('cls')
                Bill()
            elif bill != 'b':
                bill1()
        bill1()
        
    elif y == 0:
        print('สินค้าหมดค้าบเธออออ')
        supercar()
                
def sedan():
    import car
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Carinfo WHERE Typeofcar = "SEDAN" ')
    result = c.fetchall()
    print('='*175)
    o=0
    for x in result:
        o+=1
        print("\n\t\t\t\t          ",o,x[1] +'       ', x[4],'In Stock ', x[5])
    print('='*175)
    price = [0, 1000 , 2500 , 1800 , 1200 , 2500 , 1800 , 19000 , 22000 , 15000 , 35000]
    h1 = "+++++ หากไม่คืนตามนัดจะมีความผิดตามกฏหมาย +++++"
    z = int(input('โปรดเลือกรถของคุณ : '))
    namecar1 = [0,'TOYOTA Yaris','TOYOTA Camry','TOYOTA Corolla','HONDA City','HONDA Accord','HONDA Civic','E-CLASS Cabriolet','C-CLASS SALOON','BMW Z4','BMW I4']
    st = {z:namecar1[z]}
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    cc = c.execute(f"""SELECT instock FROM Carinfo where nameofcar ="{st[z]}" """)
    result = cc.fetchall()
    for i in result:
        x = list(i)
        y = int(x[0])
    s=y-1
    if s >-1:
        a = (s,st[z])
        c=conn.cursor()
        c.execute('''UPDATE Carinfo set instock = ? WHERE nameofcar = ?''',a)
        conn.commit()
        c.close()
        y = int(input('จำนวนวันที่ต้องการเช่า : ')) 
        cost.append(price[z])
        for a in cost:
            total = a*y
        print('ราคาที่ต้องชำระ คือ ',total)
        print("="*152)
        def Bill():
            c = conn.cursor()
            c.execute('''INSERT INTO rentalhistory (fname,lname,personalid,Tel,address,job,nationality,email,car,day,cost) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(info['fname'],info['lname'],info['personalid'],info['tel'],info['address'],info['job'],info['nationality'],info['email'],namecar1[z],y,total))
            conn.commit()
            print(Fore.LIGHTYELLOW_EX + '='*152)
            x = '🚗  ใบเสร็จ 🚗'
            txt=x.center(152)
            print(txt)
            print(Fore.LIGHTYELLOW_EX + '='*152)
            print("\n")
            name ="                                                              [ {}  {} ]                                                                 "
            print(name.format(info['fname'] ,info['lname']))
            print("\n") 
            id ="                                                                  [ {} ]                                                                   "
            print(id.format(info['personalid']))
            print("\n")
            add ="                                                   [ {} ]                                                                   "
            print(add.format(info['address']))
            print("\n")
            phone ="                                                   [ {} ]  [ {} ]                                                                 "
            print(phone.format(info['tel'],info['email']))
            print("\n")
            print(Fore.LIGHTYELLOW_EX + '-'*152)
            n1 ="                                                     {}                                                                                   "
            print(n1.format(car.car2))
            n ="                                                             [ {} ]                                                                                    "
            print(n.format(namecar1[z]))
            print('\n')
            b ="จำนวนวันที่เช่า   {}   วัน     ราคา   {}   บาท".center(152)
            print(b.format(y,total))
            print("\n")
            h ="                                                     {}                                                                "
            print(h.format(h1))
            print("\n")
            print('# # # # # THANK YOU # # # # #'.center(152))
            print(Fore.LIGHTYELLOW_EX + '='*152)
        def bill1():
            bill = input('พิมพ์ใบเสร็จ กด [b] : ')
            if bill == 'b':
                os.system('cls')
                Bill()
            elif bill != 'b':
                bill1()
        bill1()
        
    elif y == 0:
        print('สินค้าหมดค้าบเธออออ')
        supercar()

def pickuptruck():
    import car
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Carinfo WHERE Typeofcar = "Pickup truck" ')
    result = c.fetchall()
    print('='*175)
    o=0
    for x in result:
        o+=1
        print("\n\t\t\t\t          ",o,x[1] +'       ', x[4],'In Stock ', x[5])   
    print('='*175)
    price = [0, 2300 , 1800 , 1800]
    h1 = "+++++ หากไม่คืนตามนัดจะมีความผิดตามกฏหมาย +++++"
    z = int(input('โปรดเลือกรถของคุณ : '))
    namecar2 = [0,'Hilux Revo Prerunner & 4x4','Hilux Revo Standard Cab','NEW ISUZU D-MAX']
    st = {z:namecar2[z]}
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    cc = c.execute(f"""SELECT instock FROM Carinfo where nameofcar ="{st[z]}" """)
    result = cc.fetchall()
    for i in result:
        x = list(i)
        y = int(x[0])
    s=y-1
    if s >-1:
        a = (s,st[z])
        c=conn.cursor()
        c.execute('''UPDATE Carinfo set instock = ? WHERE nameofcar = ?''',a)
        conn.commit()
        c.close()
        y = int(input('จำนวนวันที่ต้องการเช่า : ')) 
        cost.append(price[z])
        for a in cost:
            total = a*y
        print('ราคาที่ต้องชำระ คือ ',total)
        print("="*152)
        def Bill():
            c = conn.cursor()
            c.execute('''INSERT INTO rentalhistory (fname,lname,personalid,Tel,address,job,nationality,email,car,day,cost) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(info['fname'],info['lname'],info['personalid'],info['tel'],info['address'],info['job'],info['nationality'],info['email'],namecar2[z],y,total))
            conn.commit()
            print(Fore.LIGHTYELLOW_EX + '='*152)
            x = '🚗  ใบเสร็จ 🚗'
            txt=x.center(152)
            print(txt)
            print(Fore.LIGHTYELLOW_EX + '='*152)
            print("\n")
            name ="                                                              [ {}  {} ]                                                                 "
            print(name.format(info['fname'] ,info['lname']))
            print("\n") 
            id ="                                                                  [ {} ]                                                                   "
            print(id.format(info['personalid']))
            print("\n")
            add ="                                                   [ {} ]                                                                   "
            print(add.format(info['address']))
            print("\n")
            phone ="                                                   [ {} ]  [ {} ]                                                                 "
            print(phone.format(info['tel'],info['email']))
            print("\n")
            print(Fore.LIGHTYELLOW_EX + '-'*152)
            n1 ="                                                     {}                                                                                   "
            print(n1.format(car.car3))
            n ="                                                             [ {} ]                                                                                    "
            print(n.format(namecar2[z]))
            print('\n')
            b ="จำนวนวันที่เช่า   {}   วัน     ราคา   {}   บาท".center(152)
            print(b.format(y,total))
            print("\n")
            h ="                                                     {}                                                                "
            print(h.format(h1))
            print("\n")
            print('# # # # # THANK YOU # # # # #'.center(152))
            print(Fore.LIGHTYELLOW_EX + '='*152)
        def bill1():
            bill = input('พิมพ์ใบเสร็จ กด [b] : ')
            if bill == 'b':
                os.system('cls')
                Bill()
            elif bill != 'b':
                bill1()
        bill1()
        
    elif y == 0:
        print('สินค้าหมดค้าบเธออออ')
        supercar()

def motorcycle():
    import car
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Carinfo WHERE Typeofcar = "Mortorcycle" ')
    result = c.fetchall()
    print('='*175)
    o=0
    for x in result:
        o+=1
        print("\n\t\t\t\t          ",o,x[1] +'       ', x[4],'In Stock ', x[5])
    print('='*175)
    price = [0, 250 , 562 , 570 , 600 , 250 , 642 , 500 , 600]
    h1 = "+++++ หากไม่คืนตามนัดจะมีความผิดตามกฏหมาย +++++"
    z = int(input('โปรดเลือกรถของคุณ : '))
    namecar3 = [0,'Fino 125','Aerox 155','YZF-R15','XMAX 300','New scoopy','New PCX160','ALL New CBR150R','New Forza350']
    st = {z:namecar3[z]}
    conn = sqlite3.connect(r"C:\Users\User\Desktop\code\END.db")
    c = conn.cursor()
    cc = c.execute(f"""SELECT instock FROM Carinfo where nameofcar ="{st[z]}" """)
    result = cc.fetchall()
    for i in result:
        x = list(i)
        y = int(x[0])
    s=y-1
    if s >-1:
        a = (s,st[z])
        c=conn.cursor()
        c.execute('''UPDATE Carinfo set instock = ? WHERE nameofcar = ?''',a)
        conn.commit()
        c.close()
        y = int(input('จำนวนวันที่ต้องการเช่า : ')) 
        cost.append(price[z])
        for a in cost:
            total = a*y
        print('ราคาที่ต้องชำระ คือ ',total)
        print("="*152)
        def Bill():
            c = conn.cursor()
            c.execute('''INSERT INTO rentalhistory (fname,lname,personalid,Tel,address,job,nationality,email,car,day,cost) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',(info['fname'],info['lname'],info['personalid'],info['tel'],info['address'],info['job'],info['nationality'],info['email'],namecar3[z],y,total))
            conn.commit()
            print(Fore.LIGHTYELLOW_EX + '='*152)
            x = '🚗  ใบเสร็จ 🚗'
            txt=x.center(152)
            print(txt)
            print(Fore.LIGHTYELLOW_EX + '='*152)
            print("\n")
            name ="                                                              [ {}  {} ]                                                                 "
            print(name.format(info['fname'] ,info['lname']))
            print("\n") 
            id ="                                                                  [ {} ]                                                                   "
            print(id.format(info['personalid']))
            print("\n")
            add ="                                                   [ {} ]                                                                   "
            print(add.format(info['address']))
            print("\n")
            phone ="                                                   [ {} ]  [ {} ]                                                                 "
            print(phone.format(info['tel'],info['email']))
            print("\n")
            print(Fore.LIGHTYELLOW_EX + '-'*152)
            n1 ="                                                     {}                                                                                   "
            print(n1.format(car.car4))
            n ="                                                             [ {} ]                                                                                    "
            print(n.format(namecar3[z]))
            print('\n')
            b ="จำนวนวันที่เช่า   {}   วัน     ราคา   {}   บาท".center(152)
            print(b.format(y,total))
            print("\n")
            h ="                                                     {}                                                                "
            print(h.format(h1))
            print("\n")
            print('# # # # # THANK YOU # # # # #'.center(152))
            print(Fore.LIGHTYELLOW_EX + '='*152)
        def bill1():
            bill = input('พิมพ์ใบเสร็จ กด [b] : ')
            if bill == 'b':
                os.system('cls')
                Bill()
            elif bill != 'b':
                bill1()
        bill1()
        
    elif y == 0:
        print('สินค้าหมดค้าบเธออออ')
        supercar()

while True:
    login()
    while y>'2':
        login()
    if y =='1':
        olduser()
    elif y=='2':
        newuser()
    else:
        print(Fore.LIGHTWHITE_EX + Back.RED +'ระบบผิดพลาด กรุณาทำรายการอีกครั้ง')
