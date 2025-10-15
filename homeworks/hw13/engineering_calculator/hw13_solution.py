def validate_expression(expression):
    valid_chars = "0123456789+-*/().% **"
    for char in expression:
        if char not in valid_chars:
            return False, char
    return True, None


def evaluate_expression(expression):

    is_valid, invalid_char = validate_expression(expression)

    if not is_valid:
        if invalid_char:
            return f"Invalid char --> {invalid_char}"
        return "Syntax error in the expression."

    try:
        result = eval(expression)  # pylint: disable=eval-used
        return result
    except ZeroDivisionError:
        return "Division by zero."
    except SyntaxError:
        return "Syntax error in the expression."
