# def take_attendance():
#     student_attendance = {}
#     while True:
#         student_name = input("Enter student name (or 'q' to quit): ").strip()
#         if student_name.lower() == 'q':
#             break
#         status = input(f"Is {student_name} present? (yes/no): ").strip().lower()
#         if status == 'yes':
#             student_attendance[student_name] = "Present"
#         else:
#             student_attendance[student_name] = "Absent"
#     return student_attendance

# def display_attendance(student_attendance):
#     present_count = sum(1 for status in student_attendance.values() if status == "Present")
#     absent_count = len(student_attendance) - present_count

#     print("\nAttendance Summary:")
#     print(f"Total Students: {len(student_attendance)}")
#     print(f"Present: {present_count}")
#     print(f"Absent: {absent_count}")

# if __name__ == "__main__":
#     print("Student Attendance Tracker")
#     attendance_data = take_attendance()
#     display_attendance(attendance_data)


# // USage of tkinter

import tkinter as tk
from tkinter import messagebox


def take_attendance():
    student_attendance = {}

    def add_student():
        student_name = student_entry.get().strip()
        status = status_var.get()

        if student_name:
            student_attendance[student_name] = status
            student_entry.delete(0, tk.END)  # Clear the entry field
            update_summary()
        else:
            messagebox.showwarning("Warning", "Please enter a student name.")

    def update_summary():
        present_count = sum(
            1 for status in student_attendance.values() if status == "Present"
        )
        absent_count = len(student_attendance) - present_count

        summary_label.config(
            text=f"Total Students: {len(student_attendance)}\nPresent: {present_count}\nAbsent: {absent_count}"
        )

    def quit_program():
        save_to_file(student_attendance)
        window.quit()

    def save_to_file(attendance_data):
        with open("attendance.txt", "w") as file:
            for student, status in attendance_data.items():
                file.write(f"{student}: {status}\n")

    window = tk.Tk()
    window.title("Student Attendance Tracker")

    student_label = tk.Label(window, text="Enter student name:")
    student_label.pack()

    student_entry = tk.Entry(window)
    student_entry.pack()

    status_label = tk.Label(window, text="Select attendance status:")
    status_label.pack()

    status_var = tk.StringVar(value="Present")

    present_radio = tk.Radiobutton(
        window, text="Present", variable=status_var, value="Present"
    )
    absent_radio = tk.Radiobutton(
        window, text="Absent", variable=status_var, value="Absent"
    )

    present_radio.pack()
    absent_radio.pack()

    add_button = tk.Button(window, text="Add Student", command=add_student)
    add_button.pack()

    summary_label = tk.Label(window, text="")
    summary_label.pack()

    quit_button = tk.Button(window, text="Quit", command=quit_program)
    quit_button.pack()

    window.mainloop()

    return student_attendance


if __name__ == "__main__":
    attendance_data = take_attendance()
    print("Attendance data saved to 'attendance.txt'")
    display_attendance(attendance_data)
