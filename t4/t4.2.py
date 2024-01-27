result_list = []

class DocDB:
    def __init__(self):
        self.patients = {}
        self.schedule = {}

    def add_patient(self, pid, pname, pfname, page, pheight, pweight):
        if pid not in self.patients:
            if int(page) < 0 or int(pheight) < 0 or int(pweight) < 0:
                result("error: invalid age, height, or weight")
            else:
                self.patients[pid] = {
                    'pname': pname,
                    'pfname': pfname,
                    'page': page,
                    'pheight': pheight,
                    'pweight': pweight
                }
                result("patient added successfully")
        else:
            result("error: this ID already exists")

    def display_patient(self, pid):
        if pid in self.patients:
            patient_info = self.patients[pid]
            result(f"patient name: {patient_info['pname']}")
            result(f"patient family name: {patient_info['pfname']}")
            result(f"patient age: {patient_info['page']}")
            result(f"patient height: {patient_info['pheight']}")
            result(f"patient weight: {patient_info['pweight']}")
        else:
            result("error: invalid ID")

    def add_visit(self, pid, stime):
        if pid in self.patients:
            if 9 <= int(stime) <= 18:
                if stime not in self.schedule:
                    self.schedule[stime] = self.patients[pid]
                    result("visit added successfully!")
                else:
                    result("error: busy time")
            else:
                result("error: invalid time")
        else:
            result("error: invalid id")

    def delete_patient(self, pid):
        if pid in self.patients:
            for time in list(self.schedule.keys()):
                if self.schedule[time] == self.patients[pid]:
                    self.schedule.pop(time)
            del self.patients[pid]
            result("patient deleted successfully!")
        else:
            result("error: invalid id")

    def display_visits(self, pid):
        result("SCHEDULE:")
        for time, patient_info in self.schedule.items():
            result(f"{time}:00 {patient_info['pname']} {patient_info['pfname']}")


def result(res):
    result_list.append(res)

def print_result():
    for res in result_list:
        print(res)

def main():
    doc_db = DocDB()
    pid = None  # Initialize pid

    while True:
        inp = input()
        tmp1 = inp.split()

        if inp == 'exit':
            print_result()
            break
        elif inp == 'display visit list':
            doc_db.display_visits(pid)
        elif len(tmp1) >= 3:
            cmd = tmp1[0]
            pid = tmp1[2]
            if cmd == 'add' and tmp1[1] == 'patient' and len(tmp1) == 8:
                doc_db.add_patient(pid, tmp1[3], tmp1[4], tmp1[5], tmp1[6], tmp1[7])
            elif cmd == 'display' and tmp1[1] == 'patient':
                doc_db.display_patient(pid)
            elif cmd == 'add' and tmp1[1] == 'visit' and len(tmp1) == 4:
                doc_db.add_visit(pid, tmp1[3])
            elif cmd == 'delete' and tmp1[1] == 'patient':
                doc_db.delete_patient(pid)
            else:
                result("invalid command")
        else:
            result("invalid command")

if __name__ == "__main__":
    main()

    




    