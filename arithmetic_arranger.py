# import re

def arithmetic_arranger(problems, expect_solution = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    upper_numbers = ''
    lower_numbers = ''
    operator = ''
    dash = ''
    answer = ''
    for problem in problems:
        upper_numbers = problem.split(" ")[0].strip()
        operator = problem.split(" ")[1].strip()
        lower_numbers = problem.split(' ')[2].strip()

        if (upper_numbers.isdigit() is False) or (lower_numbers.isdigit() is False):
            return "Error: Numbers must only contain digits."
            
        if (operator != '+') or (operator != '-'):
            return "Error: Operator must be '+' or '-'."
        
        if ( len(upper_numbers) or len(lower_numbers) ) >= 5 :
            return "Error: Numbers cannot be more than four digits."
        
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
