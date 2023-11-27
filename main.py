class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def medium_grade_student(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_student in list_grade:
            sum_grade += sum(grade_student)
            return sum_grade / len(grade_student)

    # def middle_grade(self):
    #     self.mid_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
    #     return self.mid_grade

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
            f'{self.medium_grade_student()}\nКурсы в процессе обучения: {",".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {",".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def medium_grade(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_lecturer in list_grade:
            sum_grade += sum(grade_lecturer)
            return sum_grade / len(grade_lecturer)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции:  {self.medium_grade()}')


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Юлия', 'Брит', 'женский')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Design']
student_2 = Student('Василий', 'Кох', 'мужской')
student_2.courses_in_progress += ['Design']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Анатолий', 'Тюрин')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Антонина', 'Моисеенко')
lecturer_2.courses_attached += ['Design']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_2, 'Design', 8)

reviewer_1 = Reviewer('Анна', 'Хорина')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Иван', 'Просеков')
reviewer_2.courses_attached += ['Design']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Design', 7)

print(student_1)
print(student_2)
print("___________\n")
print(reviewer_1)
print(reviewer_2)
print("___________\n")
print(lecturer_1)
print(lecturer_2)
print("___________\n")
print(f'Средняя оценка студентов: {(student_1.medium_grade_student() + student_2.medium_grade_student()) / 2}')
print(f'Средняя оценка лекторов: {(lecturer_1.medium_grade() + lecturer_2.medium_grade()) / 2}')
