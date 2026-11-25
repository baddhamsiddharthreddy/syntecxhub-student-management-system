import json
import os

FILE_NAME = "students.json"


class Student:
  """Represents a single student."""

  def __init__(self, student_id, name, grade):
    self.student_id = student_id
    self.name = name
    self.grade = grade

  def to_dict(self):
    return {
        "student_id": self.student_id,
        "name": self.name,
        "grade": self.grade,
    }


class StudentManager:
  """Manages student operations and JSON file persistence."""

  def __init__(self):
    self.students = self.load_students()

  def load_students(self):
    if not os.path.exists(FILE_NAME):
      return {}
    with open(FILE_NAME, "r") as file:
      data = json.load(file)
      return {
          sid: Student(sid, info["name"], info["grade"])
          for sid, info in data.items()
      }

  def save_students(self):
    with open(FILE_NAME, "w") as file:
      data = {sid: s.to_dict() for sid, s in self.students.items()}
      json.dump(data, file, indent=4)

  def add_student(self, student_id, name, grade):
    if student_id in self.students:
      print("Error: A student with this ID already exists.")
      return
    self.students[student_id] = Student(student_id, name, grade)
    self.save_students()
    print("Student added successfully!")

  def update_student(self, student_id, name, grade):
    if student_id not in self.students:
      print("Error: Student ID not found.")
      return
    self.students[student_id].name = name
    self.students[student_id].grade = grade
    self.save_students()
    print("Student updated successfully!")

  def delete_student(self, student_id):
    if student_id in self.students:
      del self.students[student_id]
      self.save_students()
      print("Student deleted successfully!")
    else:
      print("Error: Student ID not found.")

  def list_students(self):
    if not self.students:
      print("\nNo student records found.")
      return
    print("\n--- Student Records ---")
    print(f"{'ID':<10} | {'Name':<20} | {'Grade':<10}")
    print("-" * 46)
    for s in self.students.values():
      print(f"{s.student_id:<10} | {s.name:<20} | {s.grade:<10}")
    print("-" * 46)


def main():
  manager = StudentManager()

  while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. List All Students")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
      sid = input("Enter Student ID: ").strip()
      name = input("Enter Name: ").strip()
      grade = input("Enter Grade: ").strip()
      manager.add_student(sid, name, grade)

    elif choice == "2":
      sid = input("Enter Student ID to update: ").strip()
      name = input("Enter New Name: ").strip()
      grade = input("Enter New Grade: ").strip()
      manager.update_student(sid, name, grade)

    elif choice == "3":
      sid = input("Enter Student ID to delete: ").strip()
      manager.delete_student(sid)

    elif choice == "4":
      manager.list_students()

    elif choice == "5":
      print("Goodbye!")
      break

    else:
      print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
  main()