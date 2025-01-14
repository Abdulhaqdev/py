contacts = []
logout = True

def showMenu() :
    print("1. Yangi kontakt qo'shish.")
    print("2. Kontaktni yangilash.")
    print("3. Kontaktni o'chirish.")
    print("4. Kontaktni qidirish.")
    print("5. Barcha kontaktlarni ko'rsatish.")
    print("6. Chiqish.")


def EnterContact():
    name = input("Ism: ")
    
    while True:
        phone = input("Telefon raqami +998 boshlanishi kerak: ")
        if phone.startswith("+998") and len(phone) == 13 and phone[4:6] in ["77", "99", "90", "91", "93", "94", "33", "97", "95"]:
            if phone[4:6] in ['90', '91']:
                company = 'Beeline'
            elif phone[4:6] in ['93', '94']:
                company = 'Ucell'
            elif phone[4:6] == '33':
                company = 'Humans'
            elif phone[4:6] in ['99', '77', '95', '50']:
                company = 'Uzmobile'
            print("Telefon raqami to'g'ri.")
            break
        else:
            print("Xato telefon raqami! yana kiriting.")
    email = input("Email manzili: ")
    address = input('Manzil: ')
    contact = {
        'name': name,
        'phone': phone,
        'company': company,
        'email': email,
        'address': address
    }
    return contact


def AddContact() :
    contact = EnterContact()
    contacts.append(contact)
    AllContactc()


def UpdateContact():
    if not contacts:
        print("Kontaktlar ro'yxati bo'sh.")
        print()
    else:
        AllContactc()
        id = int(input(f"Qaysi birini o'zgartirmoqchisiz (1-{len(contacts)}): "))
        if id <= len(contacts) and id > 0:
            name = input(f"Ism ({contacts[id-1]['name']}): ")
            if name == '':
                name = contacts[id-1]['name']

            phone = input(f"Telefon raqami ({contacts[id-1]['phone']}): ")
            if phone == '':
                phone = contacts[id-1]['phone']

            if phone.startswith("+998") and len(phone) == 13 and phone[4:6] in ["77", "99", "90", "91", "93", "94", "33", "97", "95"]:
                if phone[4:6] in ['90', '91']:
                    company = 'Beeline'
                elif phone[4:6] in ['93', '94']:
                    company = 'Ucell'
                elif phone[4:6] == '33':
                    company = 'Humans'
                elif phone[4:6] == '98':
                    company = 'Perfectum'
                elif phone[4:6] == '71':
                    company = 'Toshkent shahar mobil operatori'
                elif phone[4:6] in ['99', '77', '95', '50']:
                    company = 'Uzmobile'
            else:
                company = contacts[id-1]['company']

            email = input(f"Email manzili ({contacts[id-1]['email']}): ")
            if email == '':
                email = contacts[id-1]['email']

            address = input(f"Manzil ({contacts[id-1]['address']}): ")
            if address == '':
                address = contacts[id-1]['address']

            contacts[id-1] = {
                'name': name,
                'phone': phone,
                'company': company,
                'email': email,
                'address': address
            }
            print(f"\n{id}-kontakt yangilandi.")
        else:
            print("Bunday kontakt yo'q!")
            UpdateContact()


def DeleteContact():
    if not contacts:
        print()
        print("Kontaktlar ro'yxati bo'sh.")
        print()
    else:
        AllContactc() 
        id = int(input(f'qaysi birini ochirmoqchisiz (1-{len(contacts)}):'))
        contacts.pop(id-1)
        print()    
        print(f'{id}-contact ochirildi!')
        print()


def SearchCOntact(): 
    search = input("Qidirish uchun ism yoki telefon raqamni kiriting: ")
    found = False
    for contact in contacts:
        if search in contact['name'] or search in contact['phone']:
            print("\nKontakt ma'lumotlari:")
            print(f"Ism: {contact['name']}")
            print(f"Telefon: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Manzil: {contact['address']}")
            found = True
    if not found:
        print("Kontakt topilmadi.")


def AllContactc() :
    if not contacts:
        print("Kontaktlar ro'yxati bo'sh.")
    else:
        print("\nBarcha kontaktlar:")
        for i in range(len(contacts)):
            print(f"{i+1}. Ism: {contacts[i]['name']}, Telefon raqami: {contacts[i]['phone']}, Companya nomi: {contacts[i]['company']} Email manzili: {contacts[i]['email']}, Manzil: {contacts[i]['address']}")
        print()


def SelectFunc():
   selected =  input('Amalyotni tanlang (1-6):')
   global  logout 
   if selected == '1' :
    AddContact()
   elif selected == '2' :
    UpdateContact()
   elif selected == '3':
    DeleteContact()
   elif selected == '4':
    SearchCOntact()
   elif selected == '5':
    AllContactc()
   elif selected == '6':
    print('Amalyot tugadi.')
    logout = False
   else:
    print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


def Main():
    while logout:
       showMenu()
       SelectFunc()

Main()