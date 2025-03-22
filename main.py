class Student:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        self.grades = []

    def add_grades(self, grades):
        if len(grades) == 4:
            self.grades = grades
        else:
            print(f"Student {self.name} requires exactly 4 grades.")

    def average_grade(self):
        if len(self.grades) != 4:
            return None
        return sum(self.grades) / 4

class GradeTracker:
    def __init__(self):
        self.students = []

    def add_student(self, name, branch, year):
        self.students.append(Student(name, branch, year))

    def add_grades(self, name, grades):
        for student in self.students:
            if student.name == name:
                student.add_grades(grades)
                return
        print(f"Student {name} not found!")

    def get_average_grade(self, name):
        for student in self.students:
            if student.name == name:
                average = student.average_grade()
                if average is not None:
                    return average
                else:
                    print(f"Student {name} does not have 4 grades yet.")
        return None

    def display_students_above_threshold(self, threshold=9):
        for student in self.students:
            average = student.average_grade()
            if average is not None and average > threshold:
                print(f"Student {student.name} from {student.branch} year {student.year} is above the threshold with an average grade of {average:.2f}.")

    def display_students_below_threshold(self, threshold=6):
        for student in self.students:
            average = student.average_grade()
            if average is not None and average < threshold:
                print(f"Student {student.name} from {student.branch} year {student.year} is below the threshold with an average grade of {average:.2f}.")

def main():
    print("Welcome to student grade tracker")
    tracker = GradeTracker()

    while True:
        print("\nOptions:")
        print("1. Add a student")
        print("2. Record grades")
        print("3. Calculate average grade")
        print("4. Display students above threshold")
        print("5. Display students below threshold")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            branch = input("Enter student branch: ")
            year = input("Enter student year: ")
            tracker.add_student(name, branch, year)
        elif choice == '2':
            name = input("Enter student name: ")
            grades = []
            for i in range(4):
                grade = float(input(f"Please enter grade for sem{i+1}: "))
                grades.append(grade)
            tracker.add_grades(name, grades)
        elif choice == '3':
            name = input("Enter student name: ")
            average = tracker.get_average_grade(name)
            if average is not None:
                print(f"The average grade for {name} is {average:.2f}")
        elif choice == '4':
            tracker.display_students_above_threshold()
        elif choice == '5':
            tracker.display_students_below_threshold()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
