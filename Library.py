class Member:
    name_member = ""
    phone_number = ""
    name_book = []

    def __init__(self, name, phonenumber, rentbook=[]): # init 왜 필요함? 그냥 아무 메서드 쓰면 안 됨? 차이가 뭐?
        self.name_member = name
        self.phone_number = phonenumber
        self.name_book = rentbook

class Library:
    member_list = []

    def regist_member(self, name, phonenumber):
        new_member = Member(name, phonenumber)
        self.member_list.append(new_member)

    def rent_book(self, name, rentbook):
        for member in self.member_list:
            if member.name_member == name:
                member.name_book.append(rentbook)

    def show_memberlist(self):
        for member in self.member_list:
            print(member.name_member, member.phone_number, member.name_book)

library = Library()
library.regist_member("이주혜", "010-5175-3795")
library.rent_book("이주혜", "파이썬어려워")
library.rent_book("이주혜", "살려줘")
library.regist_member("곱단이", "010-1234-5678")
library.rent_book("체리코코", "귀여워")
library.show_memberlist()
