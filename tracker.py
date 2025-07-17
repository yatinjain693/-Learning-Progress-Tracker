import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"WeeklyGoal": {"target": 0, "time_target": 0}, "Courses": {}}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def progress_bar(percent, width=30):
    filled = int(width * percent // 100)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {percent:.1f}%"

def add_course(data):
    course_name = input("Enter course name: ").strip()
    if course_name in data["Courses"]:
        print(f"Course '{course_name}' already exists!")
    else:
        data["Courses"][course_name] = {"Modules": {}}
        print(f"Course '{course_name}' added successfully!")
        save_data(data)

def delete_course(data):
    course_name = input("Enter course name to delete: ").strip()
    if course_name in data["Courses"]:
        del data["Courses"][course_name]
        print(f"Course '{course_name}' deleted.")
        save_data(data)
    else:
        print(f"Course '{course_name}' not found!")

def add_module(data):
    course_name = input("Enter course name: ").strip()
    if course_name not in data["Courses"]:
        print(f"Course '{course_name}' not found!")
        return
    module_name = input("Enter module name: ").strip()
    if module_name in data["Courses"][course_name]["Modules"]:
        print(f"Module '{module_name}' already exists in '{course_name}'!")
    else:
        data["Courses"][course_name]["Modules"][module_name] = {
            "status": "pending",
            "TimeSpent": 0
        }
        print(f"Module '{module_name}' added to '{course_name}'!")
        save_data(data)

def delete_module(data):
    course_name = input("Enter course name: ").strip()
    if course_name not in data["Courses"]:
        print(f"Course '{course_name}' not found!")
        return
    module_name = input("Enter module name to delete: ").strip()
    if module_name in data["Courses"][course_name]["Modules"]:
        del data["Courses"][course_name]["Modules"][module_name]
        print(f"Module '{module_name}' deleted from '{course_name}'.")
        save_data(data)
    else:
        print(f"Module '{module_name}' not found in '{course_name}'.")

def complete_module(data):
    course_name = input("Enter course name: ").strip()
    if course_name not in data["Courses"]:
        print(f"Course '{course_name}' not found!")
        return
    module_name = input("Enter module name: ").strip()
    if module_name not in data["Courses"][course_name]["Modules"]:
        print(f"Module '{module_name}' not found in '{course_name}'!")
    else:
        data["Courses"][course_name]["Modules"][module_name]["status"] = "complete"
        try:
            time_spent = int(input("Enter time spent on module (in minutes): "))
            data["Courses"][course_name]["Modules"][module_name]["TimeSpent"] += time_spent
        except ValueError:
            print("Invalid time input. Skipping time update.")
        print(f"Module '{module_name}' marked as complete!")
        save_data(data)

def view_progress(data):
    if not data["Courses"]:
        print("No courses available!")
        return

    print("\n Overall Module Completion Summary:")
    total_modules = 0
    completed_modules = 0
    total_time_spent = 0

    for course, details in data["Courses"].items():
        modules = details["Modules"]
        total_modules += len(modules)
        completed_modules += sum(1 for m in modules.values() if m["status"] == "complete")
        total_time_spent += sum(m["TimeSpent"] for m in modules.values())

    percent = (completed_modules / total_modules) * 100 if total_modules else 0
    print(f" Modules Completed: {completed_modules}/{total_modules} ({percent:.1f}%)")
    print(" Progress:", progress_bar(percent))
    hours = total_time_spent // 60
    minutes = total_time_spent % 60
    print(f" Total Time Spent Across All Modules: {hours} hr {minutes} min")


def set_weekly_goal(data):
    try:
        target = int(input("Enter weekly goal (number of modules to complete): "))
        time_target = int(input("Enter weekly time goal (in minutes): "))
        if target < 0 or time_target < 0:
            print("Goals cannot be negative!")
        else:
            data["WeeklyGoal"]["target"] = target
            data["WeeklyGoal"]["time_target"] = time_target
            print(f"Weekly goals set: {target} modules, {time_target} minutes")
            save_data(data)
    except ValueError:
        print("Please enter valid numbers!")

def track_weekly_progress(data):
    target = data["WeeklyGoal"]["target"]
    time_target = data["WeeklyGoal"]["time_target"]
    completed = 0
    total_time = 0
    for course in data["Courses"].values():
        for module in course["Modules"].values():
            if module["status"] == "complete":
                completed += 1
                total_time += module.get("TimeSpent", 0)

    module_percent = (completed / target) * 100 if target else 0
    time_percent = (total_time / time_target) * 100 if time_target else 0

    print(f"\nWeekly Goal: {target} modules")
    print(f"Completed: {completed} modules")
    print("Module Progress: ", progress_bar(module_percent))
    print(f"\nWeekly Time Goal: {time_target} minutes")
    print(f"Time Logged: {total_time} minutes")
    print("Time Progress:   ", progress_bar(time_percent))

    if completed >= target:
        print("🎉 Modules goal achieved!")
    else:
        print(f"📚 {target - completed} modules remaining.")
    if total_time >= time_target:
        print("🔥 Time goal achieved!")
    else:
        print(f"⏳ {time_target - total_time} minutes to go.")

def reset_weekly_progress(data):
    for course in data["Courses"].values():
        for module in course["Modules"].values():
            module["status"] = "pending"
            module["TimeSpent"] = 0
    print(" Weekly progress reset! All modules marked pending and time cleared.")
    save_data(data)

def main():
    data = load_data()
    while True:
        print("\n Learning Progress Tracker Menu")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Add Module")
        print("4. Delete Module")
        print("5. Complete Module")
        print("6. View Progress")
        print("7. Set Weekly Goal")
        print("8. Track Weekly Progress")
        print("9. Reset Weekly Progress")
        print("10. Exit & Save Progress")

        choice = input("Enter your choice (1–10): ").strip()

        if choice == "1":
            add_course(data)
        elif choice == "2":
            delete_course(data)
        elif choice == "3":
            add_module(data)
        elif choice == "4":
            delete_module(data)
        elif choice == "5":
            complete_module(data)
        elif choice == "6":
            view_progress(data)
        elif choice == "7":
            set_weekly_goal(data)
        elif choice == "8":
            track_weekly_progress(data)
        elif choice == "9":
            reset_weekly_progress(data)
        elif choice == "10":
            save_data(data)
            print(" Progress saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1–10.")

if __name__ == "__main__":
    main()
