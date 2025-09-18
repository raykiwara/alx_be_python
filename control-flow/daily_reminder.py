#script that reminds the user about a single, priority task for the day based on time sensitivity.

#prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no):  ")

#process task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
