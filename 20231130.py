class student:
    def __init__(self,schoolname,schooladdress,id):
        self.schoolname = schoolname
        self.schooladdress = schooladdress
        self.id = id

        def get_schoolname(self):
            return self.schoolname

        def set_schoolname(self,value):
            self.schoolname=value

        def get_schooaddress(self):
            return self.schooladdress

        def set_schooladdress(self,value):
            self.schooladdress=value

        def get_id(self):
            return self.id

        def set_id(self,value):
            self.id=value



st1 = student("11","00","11")
print(st1.get_schoolname())
print(st1.get_schooladdress())
print(st1.get_id())

st1.set_schoolname("南台科大")
print(st1.set_schoolname())

