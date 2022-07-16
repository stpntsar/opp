stut_list =[]
lectut_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        stut_list.append(self.grades)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def lec_ave(self):
        sum1 = 0
        sum2 = 0
        for val in self.grades.values():
            for n in val:
                sum2 += 1
                sum1 += n
        return round((sum1 / sum2), 1)

    def __lt__(self, lec):
        if not isinstance(lec, Lecturer):
            print('Not a Student!')
            return
        return self.lec_ave() < lec.lec_ave()

    def __str__(self):
        cours = ', '.join(self.courses_in_progress)
        finish = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.lec_ave()}\nКурсы в процессе изучения: {cours}\nЗавершенные курсы: {finish}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lectut_list.append(self.grades)

    def lec_ave(self):
        sum1 = 0
        sum2 = 0
        for val in self.grades.values():
            for n in val:
                sum2 += 1
                sum1 += n
        return round((sum1 / sum2), 1)

    def __lt__(self, stud):
        if not isinstance(stud, Student):
            print('Not a Student!')
            return
        return self.lec_ave() < stud.lec_ave()

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lec_ave()} '
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}'
        return res


def studetn(self):
    sum1 = 0
    se = 0
    courses = input('Введите названия курса студентов: ')
    for n in self:
        for key, valeu in n.items():
            if key == courses:
                for rek in valeu:
                    se += 1
                    sum1 += rek
# как тут прописать правильно, если нет такого курса?
# пытаюсь else поставить в конце, всегда выводит "Нет такого курса" даже если он есть.
    return f'Средняя оценка всех учеников по курсу {courses} : {sum1/se}'

def lecturer(self):
    sum1 = 0
    se = 0
    courses = input('Введите названия курса лекторов: ')
    for n in self:
        for key, valeu in n.items():
            if key == courses:
                for rek in valeu:
                    se += 1
                    sum1 += rek             # как тут прописать правильно, если нет такого курса?
    return f'Средняя оценка всех лекторов по курсу {courses} : {sum1/se}'


vova_student = Student('Вова', 'Пупкин', 'your_gender')
dima_student = Student('Дима', 'Петров', 'your_gender')

misha_lecturer = Lecturer('Михаил', 'Федосеев')
vit_lecturer = Lecturer('Виталий', 'Смирнов')

roma_reviewer = Reviewer('Роман', 'Ширмов')
sasha_reviewer = Reviewer('Александр', 'Семенов')



vova_student.courses_in_progress += ['Python', 'git', 'java']
vova_student.finished_courses += ['web']
dima_student.courses_in_progress += ['Python', 'git', 'java']
dima_student.finished_courses += ['web']

misha_lecturer.courses_attached += ['Python', 'git', 'java']
vit_lecturer.courses_attached += ['Python', 'git', 'java']

roma_reviewer.courses_attached += ['Python', 'git', 'java']
sasha_reviewer.courses_attached += ['Python', 'git', 'java']

roma_reviewer.rate_hw(vova_student, 'Python', 6)
roma_reviewer.rate_hw(vova_student, 'Python', 5)
roma_reviewer.rate_hw(dima_student, 'Python', 4)
roma_reviewer.rate_hw(dima_student, 'Python', 5)
sasha_reviewer.rate_hw(vova_student, 'git', 3)
sasha_reviewer.rate_hw(vova_student, 'git', 6)
sasha_reviewer.rate_hw(dima_student, 'git', 3)
sasha_reviewer.rate_hw(dima_student, 'git', 6)
sasha_reviewer.rate_hw(dima_student, 'git', 3)
roma_reviewer.rate_hw(vova_student, 'java', 8)
roma_reviewer.rate_hw(vova_student, 'java', 6)
sasha_reviewer.rate_hw(dima_student, 'java', 9)
sasha_reviewer.rate_hw(dima_student, 'java', 2)

vova_student.rate_hw(misha_lecturer, 'Python', 8)
dima_student.rate_hw(vit_lecturer, 'Python', 4)
vova_student.rate_hw(misha_lecturer, 'Python', 7)
dima_student.rate_hw(vit_lecturer, 'Python', 5)
vova_student.rate_hw(misha_lecturer, 'git', 8)
dima_student.rate_hw(vit_lecturer, 'git', 5)
vova_student.rate_hw(misha_lecturer, 'git', 7)
dima_student.rate_hw(vit_lecturer, 'git', 5)
vova_student.rate_hw(misha_lecturer, 'java', 8)
dima_student.rate_hw(vit_lecturer, 'java', 3)
vova_student.rate_hw(misha_lecturer, 'java', 7)
dima_student.rate_hw(vit_lecturer, 'java', 9)

# print(vova_student)
# print(dima_student)
# print(misha_lecturer)
# print(vit_lecturer)
# print(roma_reviewer)
# print(sasha_reviewer)
# print(vova_student > misha_lecturer)
# print(vova_student < misha_lecturer)
print(lecturer(lectut_list))
print(studetn(stut_list))



