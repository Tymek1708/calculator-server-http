# Function to check if input request operation is valid
def operation_is_valid(operation: str) -> bool:
    return operation in ["add", "sub", "mult", "div"]

# Function to check if client is dividing by 0
def div_by_zero(op: str, num2: float):
    return op == "div" and num2 == 0