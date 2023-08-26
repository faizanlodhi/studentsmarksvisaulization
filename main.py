import matplotlib.pyplot as plt

students = []

def add_student():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = []
    marks = []
    for index in range(num_subjects):
        subject = input(f"Enter subject {index+1}: ")
        subjects.append(subject)
        mark = float(input(f"Enter marks for {subject}: "))
        if mark > 100:
            print("Invalid marks. Maximum marks should be 100.")
            return
        marks.append(mark)
    students.append({"name": name, "subjects": subjects, "marks": marks})

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_report():
    for student in students:
        print(f"Student: {student['name']}")
        for subject, mark in zip(student['subjects'], student['marks']):
            print(f"{subject}: {mark}")
        average = calculate_average(student['marks'])
        print(f"Average Marks: {average:.2f}")
        print()
    visualize_averages()

def visualize_averages():
    student_names = [student['name'] for student in students]
    averages = [calculate_average(student['marks']) for student in students]

    plt.figure(figsize=(10, 6))
    plt.bar(student_names, averages)
    plt.title("Average Marks of Students")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("1. Add Student")
        print("2. Display Report")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_report()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
