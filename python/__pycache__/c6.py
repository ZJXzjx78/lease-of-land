class Student():

    sum = 0
    def __init__(self,name,age):
     
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
     
    def marking(self,score):
       
        if score < 0:
            return "不可以打负分"
        self.__score = score
        print(self.name + '同学本次考试分数为：' + str(self.__score))

    def do_homework(self):
        self.do_english_homework()
        print('homework')
   
    def do_english_homework():
        print()
    @classmethod  
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
         
    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('This is a static method ')

student1 = Student('施工队',15)
result = student1.marking(59)
print(result)
student1.__score = -1

#  student1.do_homework()
#  student1.score = -1
# student1.add(1,2)
# Student.add(1,2)
# student1.plus_sum()
# Student.plus_sum()
# Student.plus_sum()
# student2 = Student('最下面',15)
# Student.plus_sum()
# student3 = Student('百搭',15)
# Student.plus_sum()