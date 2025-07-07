import json
import os

# File to store data
DATA_FILE = "data.json"

# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"WeeklyGoal": {"target": 0}, "Courses": {}}

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new course
def add_course(data):
    course_name = input("Enter course name: ").strip()
    if course_name in data["Courses"]:
        print(f"Course '{course_name}' already exists!")
    else:
        data["Courses"][course_name] = {"Modules": {}}
        print(f"Course '{course_name}' added successfully!")
        save_data(data)

# Add a module to a course
def add_module(data):
    course_name = input("Enter course name: ").strip()
    if course_name not in data["Courses"]:
        print(f"Course '{course_name}' not found!")
        return
    module_name = input("Enter module name: ").strip()
    if module_name in data["Courses"][course_name]["Modules"]:
        print(f"Module '{module_name}' already exists in '{course_name}'!")
    else:
        data["Courses"][course_name]["Modules"][module_name] = "pending"
        print(f"Module '{module_name}' added to '{course_name}'!")
        save_data(data)

# Mark a module as complete
def complete_module(data):
    course_name = input("Enter course name: ").strip()
    if course_name not in data["Courses"]:
        print(f"Course '{course_name}' not found!")
        return
    module_name = input("Enter module name: ").strip()
    if module_name not in data["Courses"][course_name]["Modules"]:
        print(f"Module '{module_name}' not found in '{course_name}'!")
    else:
        data["Courses"][course_name]["Modules"][module_name] = "complete"
        print(f"Module '{module_name}' marked as complete!")
        save_data(data)

# View progress for all courses
def view_progress(data):
    if not data["Courses"]:
        print("No courses available!")
        return
    for course, details in data["Courses"].items():
        print(f"\nCourse: {course}")
        modules = details["Modules"]
        if not modules:
            print("  No modules added.")
        else:
            completed = sum(1 for status in modules.values() if status == "complete")
            total = len(modules)
            print(f"  Modules Completed: {completed}/{total}")
            for module, status in modules.items():
                print(f"    {module}: {status}")

# Set weekly goal
def set_weekly_goal(data):
    try:
        target = int(input("Enter weekly goal (number of modules to complete): "))
        if target < 0:
            print("Goal cannot be negative!")
        else:
            data["WeeklyGoal"]["target"] = target
            print(f"Weekly goal set to {target} modules!")
            save_data(data)
    except ValueError:
        print("Please enter a valid number!")

# Track weekly progress
def track_weekly_progress(data):
    target = data["WeeklyGoal"]["target"]
    if target == 0:
        print("No weekly goal set!")
        return
    completed = 0
    for course in data["Courses"].values():
        completed += sum(1 for status in course["Modules"].values() if status == "complete")
    print(f"Weekly Goal: {target} modules")
    print(f"Completed: {completed} modules")
    if completed >= target:
        print("🎉 Congratulations! You've met or exceeded your weekly goal!")
    else:
        print(f"Keep going! You need {target - completed} more modules to reach your goal.")

# Main CLI menu
def main():
    data = load_data()
    while True:
        print("\nLearning Progress Tracker")
        print("1. Add Course")
        print("2. Add Module")
        print("3. Complete Module")
        print("4. View Progress")
        print("5. Set Weekly Goal")
        print("6. Track Weekly Progress")
        print("7. Exit & Save Progress")
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_course(data)
        elif choice == "2":
            add_module(data)
        elif choice == "3":
            complete_module(data)
        elif choice == "4":
            view_progress(data)
        elif choice == "5":
            set_weekly_goal(data)
        elif choice == "6":
            track_weekly_progress(data)
        elif choice == "7":
            save_data(data)
            print("Progress saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-7.")
if __name__ == "__main__":
    main()