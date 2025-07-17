# 📚 Learning Progress Tracker

A simple command-line tool to help you stay on top of your learning goals by tracking courses, modules, and time spent. Whether you're working through tutorials, brushing up on skills, or prepping for interviews—this tracker keeps your progress organized and your motivation fueled.

## 🚀 Features

- **Course & Module Management**
  - Add or delete courses and modules
  - Mark modules as complete with time spent
- **Progress Visualization**
  - Progress bars show module and time completion
  - Overall learning summary and time tracking
- **Weekly Goals**
  - Set custom weekly goals (module count + time)
  - Track achievement and remaining effort
- **Reset Progress**
  - Reset weekly progress to begin fresh each week

## 🛠️ How It Works

Run the script and use the menu-driven interface to interact with the tracker:

```bash
python tracker.py
```

Then follow the prompts to:
- Add or delete courses/modules
- Complete modules with time spent
- Set goals and view progress

Progress is stored in a local `data.json` file, so your learning history is saved between sessions.

##  Example Usage

```text
1. Add Course
2. Delete Course
3. Add Module
...
10. Exit & Save Progress
Enter your choice (1–10): 1
Enter course name: Backend Mastery


Progress bar output:

Total Time Spent: 4 hr 30 min


## 💾 Data Structure

```json
{
  "WeeklyGoal": {
    "target": 50,
    "time_target": 300
  },
  "Courses": {
    "Course Name": {
      "Modules": {
        "Module Name": {
          "status": "complete",
          "TimeSpent": 45
        }
      }
    }
  }
}
