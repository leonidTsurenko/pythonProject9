class Student:
    count_of_Student = 0

    def __init__(self, name=None, height=160, mental_ability=10.0):
        self.name = name
        self.height = height
        self.mental_ability = mental_ability
        Student.count_of_Student += 1
        print('я собака')

    def study(self, mental_ability=0.5):
        self.mental_ability += mental_ability
        print('я ем ')

    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f'Я {self.name}, мій зріст {self.height} см.\nМоя розумова здібність - {self.mental_ability}.'

    def __del__(self):
        print(f'Привіт, я {self.name}, і я пішов ((')


#serg = Student(height=180)
#print(serg)
#print(serg.name)
# print(serg.count_of_Student)

собака = Student(name='собака', height=165)
print(Artur)
#print(Artur.name)
собака.grow(10)
собака.study(2)
print(собака)

# print(собака.count_of_Student)
# print(собака.count_of_Student)
# print(Student.count_of_Student)