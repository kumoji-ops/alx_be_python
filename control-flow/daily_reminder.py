task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        pr = "high"
    case "medium":
        pr = "medium"
    case "low":
        pr = "low"
    case _:
        pr = "unknown"

if time_bound == "yes":
    print(f"\nReminder: '{task}' is a {pr} priority task that requires immediate attention today!")
else:
    print(f"\nNote: '{task}' is a {pr} priority task. Consider completing it when you have free time.")
