users={}
students={}
class menu:
    def __init__(self, current_menu='log in/sign up menu'):
        self.current_menu = current_menu
        self.show_course_list = {}
        self.capcourse={}
        self.courses = {}


    def signup(self, t, i, p):
        global alist
        v1=True
        v2=False
        if len(p) < 4:
            v1 = False


        passlist = ['.', '*', '!', '$', '@', '%', '^', '&', '(', ')']
        for q in range(len(alist[9])):
            for w in passlist:
                if alist[9][q] == w:
                    v2=True
        if not (t == '-S' or t == '-P'):
            return "invalid type"
        elif (i.isdigit()==False) or alist[6]!='-n':
            return "invalid id"
        elif alist[8]!='-p':
            return "invalid name"
        elif (v1 and v2) == False:
            return "invalid password"
        elif i in users.keys():

            return "id already exists"

        else:
            users[i] = [p, t]


            return "signed up successfully!"

    def login(self, i, p):



        if i not in users.keys():
            return "incorrect id"
        elif p not in (users[i]):

            return "incorrect password"
        else:
            if '-S' in users[i]:
                self.current_menu = "student menu"
            elif '-P' in users[i]:

                self.current_menu = "professor menu"
            return f"logged in successfully!\nentered {self.current_menu}"


    def logout(self):
        self.current_menu = "log in/sign up menu"
        return f"logged out successfully!\nentered {self.current_menu}"


    def add_course(self, cn, ci, cap, ts=0):
        self.cn = cn
        self.ci = ci
        self.cap = cap
        self.ts = ts
        if alist[5] != '-i':
            return "invalid course name"
        elif alist[6].isdigit() == False:
            return "invalid course id"
        elif alist[8].isdigit() == False:
            return "invalid course capacity"
        elif ci in self.show_course_list.keys():
            return "course id already exists"
        else:
            self.show_course_list[str(ci)] = f"{ci} {cn} {ts}/{cap}"
            self.capcourse[str(ci)]=f"{cap}"
            return "course added successfully!"




    def get_course(self, ci, ts=0):
        for p in users.keys():
            if users[p][1]=='-S':
                students[p]= users[p]
        i=students[-1]
        if ci not in self.show_course_list.keys():
            return "incorrect course id"
        elif i in self.courses[ci]:
            return "you already have this course"
        elif len(self.courses[ci]) >= self.capcourse[ci]:
            return "course is full"
        else:
            ts += 1
            self.courses[ci].append(i)
            return "course added successfully!"

m = menu()
input_commands = []

while True:
    a = input().strip()
    if a == "edu exit edu":
        break
    input_commands.append(a)

for a in input_commands:
    alist = a.split(' ')

    if a == "edu current menu edu":
        print(f'{m.current_menu}')
    elif (alist[1] == 'sign' and alist[2] == 'up'):
        print(m.signup(alist[3], alist[5], alist[9]))
    elif (alist[1] == 'log' and alist[2] == 'in' and alist[3] == '-i' and (alist[6] == '-p' or alist[5] == '-p')):
        print(m.login(alist[4], alist[6]))
    elif alist[1] == 'get' and alist[2] == 'course' and m.current_menu == 'student menu' and alist[3] == '-i':
        print(m.get_course(alist[4]))
    elif alist[1] == 'add' and alist[2] == 'course' and alist[3] == '-c' and (
            alist[6] == '-i' or alist[5] == '-i') and (
            alist[7] == '-n' or alist[8] == '-n') and m.current_menu == 'professor menu':
        print(m.add_course(alist[4], alist[6], alist[8]))
    elif a == 'edu show course list edu' and m.current_menu != 'log in/sign up menu':
        print('course list:')
        for i in m.show_course_list.values():
            print(i)
    elif a == 'edu log out edu' and m.current_menu != 'log in/sign up menu':
        print(m.logout())
    else:
        print("invalid command")








    




    