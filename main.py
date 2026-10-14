task_name = input("Enter task name:")
priority_level = int(input("Enter priority level (1-3): "))
estimated_hours = float(input("Enter estimated hours: "))
study_days_available = int(input("Enter available study days: "))
daily_hours_target = estimated_hours / study_days_available


print()
print("Task:", task_name)
print("Priority:", priority_level)
print("Daily Study Target:", daily_hours_target, "hours")
