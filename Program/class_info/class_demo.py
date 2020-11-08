class student():
    def __init__(self,name=None,score=0):
        self.name=name
        self.score=score
    def run(self):
        pass
    def read(self):
        pass

class good_student(student):
    def __init__(self,name=None,score=0,age=18):
        super().__init__(name,score)
        self.age=age
    def dance(self):
        pass

s=student(name="A",score=90)
gs=good_student(name="B",score=85)

print(dir(s))
print(dir(student))
print(dir(gs))
print(dir(good_student))