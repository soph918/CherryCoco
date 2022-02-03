lDB = {}

def register():
    name = input("이름은? : ")
    number = int(input("핸드폰 번호는? : "))
    book = "-"
    lDB[name] = [number, book]

def changenumber(name, number):
    lDB[name] = [number, lDB[name][1]]

def delete(name):
    lDB.pop(name)

def borrowbook(name, book):
    lDB[name] = [lDB[name][0], book]

def returnbook(name):
    lDB[name] = [lDB[name][0], '-']

