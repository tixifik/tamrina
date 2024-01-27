finalresult = list()

class docdb:
    



    def __init__(self):
        
        self.p = {}
        self.sch = {}
        
    



    def addp(self, pid, pname, pfname, page, pheight, pweight):

        if pid not in self.p:
            
            if int(page) < 0:
                result("error: invalid age")


            elif int(pheight) < 0:
                result("error: invalid height")


            elif int(pweight) < 0:
                result("error: invalid weight")
                        

            else:
                self.p[pid] = {
                    'pname': pname,
                    'pfname': pfname,
                    'page': page,
                    'pheight': pheight,
                    'pweight': pweight
                }

                result("patient added successfully")


        else:
            result("error: this ID already exists")




    def dispp(self, pid):
        if pid in self.p:

            pinfo = self.p[pid]

            result(f"patient name: {pinfo['pname']}") 
            result(f"patient family name: {pinfo['pfname']}")
            result(f"patient age: {pinfo['page']}")
            result(f"patient height: {pinfo['pheight']}")
            result(f"patient weight: {pinfo['pweight']}")


        else:
            result("error: invalid ID")




    def addvisit(self, pid, stime):
        if pid in self.p:
            if 9 <= int(stime) <= 18:
                if stime not in self.sch:
                    self.sch[stime] = self.p[pid]
                    result("visit added successfully!")

                else:
                    result("error: busy time")

            else:
                result("error: invalid time")

        else:
            result("error: invalid id")




    def delp(self, pid):
        if pid in self.p:
            
            for time in list(self.sch.keys()):
                if self.sch[time] == self.p[pid]:
                    self.sch.pop(time)

            del self.p[pid]
            result("patient deleted successfully!")

        else:
            result("error: invalid id")




    def dispvisits(self,pid):
        result("SCHEDULE:")

        
        for time, pinfo in self.sch.items():
            result(f"{time}:00 {pinfo['pname']} {pinfo['pfname']}")



def result(result):
        
        finalresult.append(result)




def presult():

    for res in finalresult:
        print(res)



def main():

    docdb1 = docdb()



    while True:

        inp = input()
        tmp1 = inp.split()


        if inp == 'exit':

            presult()
            break

        elif inp == 'display visit list':
            docdb1.dispvisits(pid)


        elif len(tmp1) >= 3:

            cmd = tmp1[0]
            pid = tmp1[2]


            if cmd == 'add' and tmp1[1] == 'patient' and len(tmp1) == 8:
                docdb1.addp(pid, tmp1[3], tmp1[4], tmp1[5], tmp1[6], tmp1[7])

            elif cmd == 'display' and tmp1[1] == 'patient':
                docdb1.dispp(pid)

            elif cmd == 'add' and tmp1[1] == 'visit' and len(tmp1)==4:    
                docdb1.addvisit(pid, tmp1[3])

            elif cmd == 'delete' and tmp1[1] == 'patient':
                docdb1.delp(pid)

            else:
                result("invalid command")

        else:
            result("invalid command")



main()
   


    




    