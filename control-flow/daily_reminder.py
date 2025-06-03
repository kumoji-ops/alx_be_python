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
        pr = priority  # just keep input if unknown

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {pr} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' is a {pr} priority task. Consider completing it when you have free time.")