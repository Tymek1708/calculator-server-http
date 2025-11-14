
def calc(op_type: str, num1: float, num2: float):
    match op_type:
        case "add":
            return num1 + num2
        case "sub":
            return num1 - num2
        case "mult":
            return num1 * num2
        case "div":
            return num1 / num2 if num2 != 0 else None
        case _:
            return None