# Function to check if input request operation is valid
def operation_is_valid(operation: str) -> bool:
    return operation in ["add", "sub", "mult", "div"]

# Function to check if client is dividing by 0
def div_by_zero(op: str, num2: float):
    return op == "div" and num2 == 0

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