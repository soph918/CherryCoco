
# 기본 기능: 회원 등록, 변경, 삭제, 대여, 반납, 도서 등록, 변경, 삭제
# 추가 예정 기능: 멤버 리스트 정보 파일, 책 정보 리스트 파일 

class Member:
    member_name = ""
    phone_number = ""
    rent_book = []

    def __init__(self, name, phonenumber): # init 왜 필요함? 그냥 아무 메서드 쓰면 안 됨? 차이가 뭐? # 여기다 rentbook=[]을 넣으면 왜 전역변수화됨?
        self.member_name = name
        self.phone_number = phonenumber
        self.rent_book = [] # 이게 왜 rentbook이면 안 됨?

class Book:
    book_name = ""
    book_author = ""

    def __init__(self, name, author):
        self.book_name = name
        self.book_author = author

class Library:
    member_list = []
    book_list = []

    def regist_member(self, name, phonenumber):
        new_member = Member(name, phonenumber)
        self.member_list.append(new_member)
    
    def regist_book(self, name, author):
        new_book = Book(name, author)
        self.book_list.append(new_book)

    def rent_book(self, name, rentbook):
        for member in self.member_list:
            if member.member_name == name:
                member.rent_book.append(rentbook)

    def return_book(self, name, returnbook):
        for member in self.member_list:
            if member.member_name == name:
                member.rent_book.remove(returnbook)
    
    def edit_member(self, name, phonenumber):
        for member in self.member_list:
            if member.member_name == name:
                member.phone_number = phonenumber

    def edit_book(self, name, author):
        for book in self.book_list:
            if book.book_name == name:
                book.book_author = author

    def remove_member(self, name):
        for member in self.member_list:
            if member.member_name == name:
                self.member_list.remove(member) # 왜 멤버가 인수로 있어야 함? 무슨 작용?

    def remove_book(self, name):
        for book in self.book_list:
            if book.book_name == name:
                self.book_list.remove(book) # 왜 멤버가 인수로 있어야 함? 무슨 작용?

    def show_memberlist(self):
        for member in self.member_list:
            print(member.member_name, member.phone_number, member.rent_book)

    def show_booklist(self):
        for book in self.book_list:
            print(book.book_name, book.book_author)  

library = Library()
# library.regist_member("이주혜", "010-5175-3795")
# library.rent_book("이주혜", "파이썬어려워")
# library.rent_book("이주혜", "살려줘")
# library.regist_member("곱단이", "010-1234-5678")
# library.rent_book("체리", "귀여워")
# library.remove_member("곱단이")
# library.edit_member("이주혜", "010-9876-5432")
# library.regist_member("코코", "010-1357-2468")
# library.return_book("이주혜", "살려줘")
# library.show_memberlist()

# library.regist_book("하얀거탑", "김명민")
# library.edit_book("하얀거탑", "이주혜")
# library.regist_book("샤모니", "밍동")
# library.remove_book("샤모니")
# library.show_booklist()

while True:
    print("1. 회원 정보 등록")
    print("2. 회원 정보 변경")
    print("3. 회원 정보 삭제")
    print("4. 회원 정보 조회")
    print("5. 도서 정보 등록")
    print("6. 도서 정보 변경")
    print("7. 도서 정보 삭제")
    print("8. 도서 목록 조회")
    print("9. 도서 대출")
    print("10. 도서 반납")
    print("11. 종료")
    print("")

    input_menu = input("원하는 메뉴를 골라주세요. ")

    if input_menu == '1':
        input_name = input("등록할 회원의 이름을 입력해주세요. ")
        input_phonenumber = input("등록할 회원의 핸드폰 번호를 입력해주세요. ")
        library.regist_member(input_name, input_phonenumber)
        print("회원 등록이 완료되었습니다. \n")
    elif input_menu == '2':
        input_name = input("정보를 변경할 회원의 이름을 입력해주세요. ")
        input_phonenumber = input("변경할 회원의 핸드폰 번호를 입력해주세요. ")
        library.edit_member(input_name, input_phonenumber)
        print("회원 정보 변경이 완료되었습니다. \n")
    elif input_menu == '3':
        input_name = input("정보를 삭제할 회원의 이름을 입력해주세요. ") 
        library.remove_member(input_name)   
        print("회원 정보 삭제가 완료되었습니다. \n")   
    elif input_menu == '4':
        library.show_memberlist()
        print("회원 리스트 조회가 완료되었습니다. \n")
    elif input_menu == '5':
        input_bookname = input("등록할 책의 이름을 입력해주세요. ")
        input_authorname = input("등록할 책의 저자를 입력해주세요. ")
        library.regist_book(input_bookname, input_authorname)
        print("책 등록이 완료되었습니다. \n")
    elif input_menu == '6':
        input_bookname = input("정보를 변경할 책의 이름을 입력해주세요. ")
        input_authorname = input("변경할 책의 저자를 입력해주세요. ")
        library.edit_book(input_bookname, input_authorname)
        print("책 저자 정보 변경이 완료되었습니다. \n")
    elif input_menu == '7':
        input_bookname = input("정보를 삭제할 책의 이름을 입력해주세요. ")
        library.remove_book(input_bookname)
        print("책 정보 삭제가 완료되었습니다. \n")
    elif input_menu == '8':
        library.show_booklist()
        print("책 리스트 조회가 완료되었습니다. \n")
    elif input_menu == '9':
        input_name = input("대출할 회원의 이름을 입력해주세요. ")
        input_bookname = input("대출할 책의 이름을 입력해주세요. ")
        library.rent_book(input_name, input_bookname)
        print("대출이 완료되었습니다. \n")
    elif input_menu == '10':
        input_changeinfo = input("반납할 회원의 이름을 입력해주세요. ")
        input_bookname = input("반납할 책의 이름을 입력해주세요. ")
        library.return_book(input_name, input_bookname)
        print("반납이 완료되었습니다 \n")
    elif input_menu == '11':
        print("프로그램을 종료합니다. \n")
        break
    else:
        print("없는 메뉴입니다. \n")
