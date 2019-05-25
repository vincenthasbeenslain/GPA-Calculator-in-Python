##Written by Vincent Nguyen
#GPA = (grades * credits)/credits

grade_to_point = {"A+": 4.3, "A": 4, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0}
unit_total = 0
credit_hours = 0
calc_state = True
while calc_state:
    user_input = input("Enter a grade or enter 'done' to finish: ").strip().capitalize()
    unit_state = True
    if user_input == "Done":
        calc_state = False
        unit_state = False
    while unit_state:
        try:
            units = float(input("Enter the units for the class: ").strip())
            credit_hours += grade_to_point[user_input] * units
            unit_total += units
            unit_state = False
        except:
            print("Error! Please enter numeric input.")
print("Your GPA is", round(credit_hours / unit_total, 2))

'''
Enter a grade or enter 'done' to finish: a
Enter the units for the class: 2
Enter a grade or enter 'done' to finish: b+
Enter the units for the class: 2
Enter a grade or enter 'done' to finish: a
Enter the units for the class: 4
Enter a grade or enter 'done' to finish: c-
Enter the units for the class: 1
Enter a grade or enter 'done' to finish: b
Enter the units for the class: 2
Enter a grade or enter 'done' to finish: b-
Enter the units for the class: 1
Enter a grade or enter 'done' to finish: a
Enter the units for the class: 1
Enter a grade or enter 'done' to finish: done
Your GPA is 3.46
'''
