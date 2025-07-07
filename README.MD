# Learning Progress Tracker

## Project Overview
This is a Python-based Command Line Interface (CLI) tool for managing courses, tracking learning progress, and setting weekly goals. It allows users to add courses and modules, mark modules as complete, view progress, set weekly goals, and track progress against those goals. Data is stored persistently in a JSON file (data.json).

## Running Instructions
1. *Prerequisites*:
   - Python 3.x installed.
   - A code editor like VS Code.
   - Git for version control.

2. *Setup*:
   - Clone this repository: git clone <your-repo-link>
   - Navigate to the project folder: cd learning-progress-tracker
   - Ensure data.json exists (a sample is provided).

3. *Run the Program*:
   - Execute the script: python tracker.py
   - Follow the CLI menu to interact with the tool (options 1-7).

4. *Features*:
   - Add a new course.
   - Add a module to an existing course.
   - Mark a module as complete.
   - View progress for all courses.
   - Set a weekly goal (number of modules to complete).
   - Track progress against the weekly goal.
   - Save progress and exit.

## JSON Structure
The data.json file stores data in the following format:
```json
{
  "WeeklyGoal": {
    "target": <number_of_modules>
  },
  "Courses": {
    "<CourseName>": {
      "Modules": {
        "<ModuleName>": "<status (complete/pending)>"
      }
    }
  }
}