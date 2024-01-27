class Menu:
    def __init__(self):
        self.current_menu = 'log in/sign up menu'
        self.show_course_list = {}
        self.cap_course = {}
        self.courses = {}
        self.users = {}
        self.students = {}

    def signup(self, user_type, user_id, password):
        if len(password) < 4:
            return "invalid password"
        
        if any(char in ['.', '*', '!', '$', '@', '%', '^', '&', '(', ')'] for char in password):
            return "invalid password"

        if user_type not in ['-S', '-P'] or not user_id.isdigit() or '-n' not in alist[6] or '-p' not in alist[8]:
            return "invalid input"

        if user_id in self.users.keys():
            return "id already exists"
        else:
            self.users[user_id] = [password, user_type]
            return "signed up successfully!"

    def login(self, user_id, password):
        if user_id not in self.users.keys():
            return "incorrect id"
        elif password not in self.users[user_id]:
            return "incorrect password"
        else:
            self.current_menu = "student menu" if '-S' in self.users[user_id] else "professor menu"
            return f"logged in successfully!\nentered {self.current_menu}"

    def logout(self):
        self.current_menu = "log in/sign up menu"
        return f"logged out successfully!\nentered {self.current_menu}"

    def add_course(self, course_name, course_id, capacity, time_slots=0):
        if '-i' not in alist[5] or not alist[6].isdigit() or not alist[8].isdigit() or course_id in self.show_course_list.keys():
            return "invalid input"
        else:
            self.show_course_list[str(course_id)] = f"{course_id} {course_name} {time_slots}/{capacity}"
            self.cap_course[str(course_id)] = f"{capacity}"
            return "course added successfully!"

    def get_course(self, course_id, time_slots=0):
        student_id = self.students[-1]
        if course_id not in self.show_course_list.keys():
            return "incorrect course id"
        elif student_id in self.courses[course_id]:
            return "you already have this course"
        elif len(self.courses[course_id]) >= self.cap_course[course_id]:
            return "course is full"
        else:
            time_slots += 1
            self.courses[course_id].append(student_id)
            return "course added successfully!"


menu_instance = Menu()
input_commands = []

while True:
    command = input().strip()
    if command == "edu exit edu":
        break
    input_commands.append(command)

for command in input_commands:
    alist = command.split(' ')

    if command == "edu current menu edu":
        print(f'{menu_instance.current_menu}')
    elif (alist[1] == 'sign' and alist[2] == 'up'):
        print(menu_instance.signup(alist[3], alist[5], alist[9]))
    elif (alist[1] == 'log' and alist[2] == 'in' and alist[3] == '-i' and (alist[6] == '-p' or alist[5] == '-p')):
        print(menu_instance.login(alist[4], alist[6]))
    elif alist[1] == 'get' and alist[2] == 'course' and menu_instance.current_menu == 'student menu' and alist[3] == '-i':
        print(menu_instance.get_course(alist[4]))
    elif alist[1] == 'add' and alist[2] == 'course' and alist[3] == '-c' and (
            alist[6] == '-i' or alist[5] == '-i') and (
            alist[7] == '-n' or alist[8] == '-n') and menu_instance.current_menu == 'professor menu':
        print(menu_instance.add_course(alist[4], alist[6], alist[8]))
    elif command == 'edu show course list edu' and menu_instance.current_menu != 'log in/sign up menu':
        print('course list:')
        for value in menu_instance.show_course_list.values():
            print(value)
    elif command == 'edu log out edu' and menu_instance.current_menu != 'log in/sign up menu':
        print(menu_instance.logout())
    else:
        print("invalid command")









    




    