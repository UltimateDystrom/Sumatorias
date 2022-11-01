import re
import math

def summatory(expression, variable, min_num, max_num):
    if "fact" in expression:
        expression = expression.replace("fact", "math.factorial")
    count = min_num
    sum = 0
    while count <= max_num:
        try:
            new_expression = expression.replace(variable, str(min_num))
            result = eval(''.join(new_expression))
            sum += result
            count += 1  
            min_num += 1
        except:
            break
    return sum

def summatory_p(expression, variable, min_num, max_num):
    if "fact" in expression:
        expression = expression.replace("fact", "math.factorial")
    l_process = []
    count = min_num
    sum = 0
    while count <= max_num:
        try:
            new_expression = expression.replace(variable, str(min_num))
            l_process.append(new_expression)
            result = eval(''.join(new_expression))
            sum += result
            count += 1  
            min_num += 1
        except:
            break
    l_process.append(str(sum))
    return l_process
    

def isRight(expression, variable):
    count_variables = 0
    if "fact" in expression:
        expression = expression.replace("fact", "")
    for i in expression:
        if i.isalpha():
            count_variables += 1

    if count_variables == 0:
        return False

    expression = list(expression)
    for i in expression:
        if i != variable:
            if i.isalpha():
                return False
        else:
            continue
    return True
