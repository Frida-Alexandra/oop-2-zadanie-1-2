class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def ave_grade(self):  # среднее за д.з студента
        a = 0  # сумма оценок
        g = 0  # количество оценок
        for course in self.grades.values():
            a += sum(course)
            g += len(course)
        if g == 0:
            return 0
        return round(a / g, 1)

    def average_grade(self, course):  # среднее за лекции
        a = 0
        g = 0
        for lection in self.grades:
            if lection == course:
                a += sum(self.grades[course])
                g += len(self.grades[course])
        if g == 0:
            return 0
        return round(a / g, 1)

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: "
                f"{self.ave_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Студентов не сравнивают с лекторами.")
            return False
        return self.ave_grade() < other.ave_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def ave_grade(self):
        a = 0  # сумма оценок
        g = 0  # количество оценок
        for course in self.grades.values():
            a += sum(course)
            g += len(course)
        if g == 0:
            return 0
        return round(a / g, 1)

    def average_grade(self, course):  # среднее за лекции
        a = 0
        g = 0
        for lection in self.grades:
            if lection == course:
                a += sum(self.grades[course])
                g += len(self.grades[course])
        if g == 0:
            return 0
        return round(a / g, 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_grade()}"

    def __lt__(self, other):  # сравнение слекторов
        if not isinstance(other, Lecturer):
            print("Лекторов не сравнивают со студентами.")
            return False
        return self.ave_grade() < other.ave_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


student_1 = Student("Петя", "Иванов", "Мужской")
student_1.courses_in_progress += ["Git"]
student_1.finished_courses += ["Python"]

student_2 = Student("Михаил", "Петрович", "Мужской")
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Git"]

lecturer_1 = Lecturer("Василий", "Алексеевич")
lecturer_1.courses_attached += ["Git"]
lecturer_1.courses_attached += ["Python"]

lecturer_2 = Lecturer("Георгий", "Петрович")
lecturer_2.courses_attached += ["Python"]

reviewer_1 = Reviewer("Максим", "Васильевич")
reviewer_1.courses_attached += ["Git"]

reviewer_2 = Reviewer("Виктор", "Иванович")
reviewer_2.courses_attached += ["Python"]

reviewer_1.rate_hw(student_1, "Git", 10)
reviewer_1.rate_hw(student_1, "Git", 8)
reviewer_1.rate_hw(student_1, "Git", 7)

reviewer_2.rate_hw(student_2, "Python", 9)
reviewer_2.rate_hw(student_2, "Python", 10)
reviewer_2.rate_hw(student_2, "Python", 9)

student_1.rate_lecturer(lecturer_1, "Git", 7)
student_1.rate_lecturer(lecturer_1, "Git", 10)

student_2.rate_lecturer(lecturer_2, "Python", 10)
student_2.rate_lecturer(lecturer_2, "Python", 5)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def student_rating(student_list, course_name): # среднее всех студентов
    sum_all = 0
    count_all = []
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.ave_grade()
            count_all.append(stud)
    return sum_all / max(len(count_all), 1)

def lecturer_rating(lecturer_list, course_name): # среднее всех лекторов
    sum_all = 0
    count_all = []
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            sum_all += lect.ave_grade()
            count_all.append(lect)
    return sum_all / max(len(count_all), 1)

print("-Задание №3-")
print("***Проверяющие***")
print("1.", reviewer_1, "\n", "2.", reviewer_2)
print()
print("***Лекторы***")
print("1.", lecturer_1, "\n", "2.", lecturer_2)
print()
print("***Студенты***")
print("1.", student_1, "\n", "2.", student_2)
print()
print("-Сравнения-")
print(
    f"Результат сравнения студентов по средним оценкам за домашние задания: "
    f"{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}"
)
print(
    f"Результат сравнения лекторов по средним оценкам за лекции: "
    f"{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}"
)
print()
print("-Задание №4-")
print(
    f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}"
)
print(
    f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}"
)
