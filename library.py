
from smtplib import SMTP

user_collection=[]

book_collection={}

class books:
    def __init__(self):
        pass
    def set_book_title(self):
        self.title=input("enter the book name: ")
    def set_book_author(self):
        self.author=input("enter the book author: ")
    def get_book_title(self):
        title=self.title
        return title
    def get_book_author(self):
        author=self.author
        return author
class booklist(books):
    def __init__(self):
        self.status="available"
        
    def add_values_in_dict(self,original_dict,key,list_of_values):
        original_dict[key]=list()
        original_dict[key].append(list_of_values)
        return original_dict
    def store_collection(self):
        global book_collection
        self.set_book_title()
        self.set_book_author()
        book_title=self.get_book_title()
        book_author=self.get_book_author()
        status=self.status

        list_of_values=[book_author,status]

        book_collection=self.add_values_in_dict(book_collection,book_title,list_of_values)
        print("book updated successfully")

    def search_collection(self):
        title=input("enter the name of the book")
        temp_dict=book_collection
        for key in temp_dict.keys():
            if title==key:
                position=key
                print("the book is found")
                print(book_collection[position])
                break
class users:
    def __init__(self):
        pass
    def create_user(self):
        self.username=input("enter the user name:")
        self.name=input("enter the name:")
        self.password=input("enter password:")
        self.email=input("enter the email:")
        self.contact=input("enter the contact number:")
    def return_username(self):
        username=self.username
        return username
    def return_name(self):
        name=self.name
        return name
    def return_password(self):
        password=self.password
        return password
    def return_email(self):
        email=self.email
        return email
    def return_contact(self):
        contact=self.contact
        return contact
class adminuser(users):
    def __init__(self):
        self.borrowing=0
    def add_values_in_list(self,original_list,list_of_values):
        original_list.append(list_of_values)
        return original_list
        
    
    def store_collection(self):
          global user_collection
          self.create_user()

          username=self.username
          name=self.name
          password=self.password
          email=self.email
          contact=self.contact
    
          list_of_values=(username,name,password,email,contact)
          user_collection=self.add_values_in_list(user_collection,list_of_values)
          print("user details")
    def user_details(self):
        username=input("enter the user name to be displayed:")
        global user_collection
        for value in user_collection:
            for i in value:
                if username==i:
                    index=user_collection.index(value)
                    print("user found")
                    return user_collection[index]
class LT(users):
        
    def borrow_book(self):
        book_name=input("enter the book name you want to borrow:")
        username=input("enter your username:")

        global book_collection
        global user_collection

        for key in book_collection.keys():
            if key==book_name:
                book_collection[book_name][0][6]='unavailable'
                book_collection[book_name][0][7]=book_collection[book_name][0][7]+username+','
        for value in user_collection:
            for i in value:
                if i==username:
                    index=user_collection.index(value)
                    user_collection[index][8]=user_collection[index][8]+1
                    user_collection[index][9]=user_collection[index][9]+book_name+','
                    print("book has been issued at your name")
                    break
        sender_email="LTS@gmail.com"
        receiver_email=input("enter email:")
        password=input("enter password:")
        message="hey,book was borrowed"
        print("login success")
        print(message)
        print("email has been sent to",receiver_email)
    def return_book(self):
        book_name=input("enter the book name you want to return:")
        username=input("enter the username:")

        global book_collection
        global user_collection

        if book_name in book_collection.keys():
            book_collection[book_name][0][6]='available'
        for value in user_collection:
            for i in value:
                if username==i:
                    index=user_collection.index(value)
                    user_collection[index][8]=user_collection[index][8]-1
                    user_collection[index][9]=user_collection[index][9].replace(book_name+',')
                    book_collection[book_name][0][7]=book_collection[book_name][0][7].replace(username+',')
                    print("book has been returned by you")
                    break
        sender_email="LTS@gmail.com"
        receiver_email=input("enter email:")
        password=input("enter password:")
        message="hey,book was returned"
        print("login success")
        print(message)
        print("email has been sent to",receiver_email)                                                                   
       
book_collection={}
user_collection=[]

booklist=booklist()
adminuser=adminuser()
LT=LT()

print("welcome to library management system")
print("----------------------------------------------------------------------------------------------")
print()
proceed='yes'
while(proceed=='yes' or proceed=='yes'):
    print("select an option from the list: ")
    print("---------------------------------------------------------------------------------")
    print()
    print("1.press 1 for searching a book in library")
    print("2.press 2 for searching user details in library")
    print("3.press 3 for you want to borrow")
    print("4.press 4 for a book returnded")

    print("press No to exit library management system")

    order=int(input("please select an option by entering an number: "))
    if(order==1):
        booklist.store_collection()
    elif(order==2):
        adminuser.store_collection()
    elif(order==3):
        LT.borrow_book()
    elif(order==4):
        LT.return_book()
    print("press yes to proceed, press No to exit")
    proceed=input("enter your choice:")
else:
    print("thank you for visiting LMS")
