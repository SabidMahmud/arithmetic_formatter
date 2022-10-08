def arithmetic_arranger(problems, expect_solution = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    upper_line = ''
    operator_line = ''
    dash_bar = ''
    answer_line = ''
    for problem in problems:
        upper_numbers = problem.split(" ")[0].strip()
        operator = problem.split(" ")[1].strip()
        lower_numbers = problem.split(' ')[2].strip()

        if (upper_numbers.isdigit() is False) or (lower_numbers.isdigit() is False):
            return "Error: Numbers must only contain digits."
            
        if (operator != '+') and (operator != '-'):
            return "Error: Operator must be '+' or '-'."
        
        if ( len(upper_numbers) > 4 or len(lower_numbers) > 4 ):
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(upper_numbers), len(lower_numbers)) + 2

        if operator == '+':
            result = str(int(upper_numbers) + int(lower_numbers))
        elif operator == '-':
            result = str(int(upper_numbers) - int(lower_numbers))
        
        # formation part // right justified //
        top_line = upper_numbers.rjust(width)
        second_line = operator + lower_numbers.rjust(width-1)
        line = "".rjust(width, '-')
        result_line = str(result).rjust(width)
        
        if problem != problems[-1] :
            upper_line += top_line + "    "
            operator_line += second_line + "    "
            dash_bar += line + "    "
            answer_line += result_line + "    "
        else :
            upper_line += top_line
            operator_line += second_line
            dash_bar += line
            answer_line += result_line

    if expect_solution :
        return upper_line + '\n' + operator_line + '\n' + dash_bar + '\n' + answer_line
    else :
        return upper_line + '\n' + operator_line + '\n' + dash_bar

