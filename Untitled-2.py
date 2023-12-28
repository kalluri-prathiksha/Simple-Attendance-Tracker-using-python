class AttendanceTracker:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_name):
        if student_name in self.attendance:
            print(f"{student_name} is already marked present.")
        else:
            self.attendance[student_name] = True
            print(f"{student_name} marked present.")

    def display_attendance(self):
        print("\nAttendance:")
        for student, present in self.attendance.items():
            status = "Present" if present else "Absent"
            print(f"{student}: {status}")

def main():
    attendance_tracker = AttendanceTracker()

    while True:
        print("\nAttendance Tracker Menu:")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            student_name = input("Enter student name: ")
            attendance_tracker.mark_attendance(student_name)
        elif choice == "2":
            attendance_tracker.display_attendance()
        elif choice == "3":
            print("Exiting the attendance tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
