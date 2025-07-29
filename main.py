import inquirer
import re

getnumentr = lambda t: f"Enter Number { '1' if t == 1 else '2' if t == 2 else '?' }"
oprts = ["+ (Plus)", "- (Minus)", "* (Multiply)", "/ (Divide)"]

inputs = [
    inquirer.Text(
        "n1",
        message=getnumentr(1),
        validate=lambda _, x: re.match("[+-]?(\d+\.?\d*|\.?\d+)", x)
    ),
    inquirer.Text(
        "n2",
        message=getnumentr(2),
        validate=lambda _, x: re.match("[+-]?(\d+\.?\d*|\.?\d+)", x)
    ),
    inquirer.List(
        "oprt",
        message="Select operations",
        choices=oprts
    )
]

answers = inquirer.prompt(inputs)
num1 = answers["n1"]
num2 = answers["n2"]
oprt = answers["oprt"]
answer:float = ""

match (oprt):
    case "+ (Plus)":
        answer = float(num1) + float(num2)
    case "- (Minus)":
        answer = float(num1) - float(num2)
    case "* (Multiply)":
        answer = float(num1) * float(num2)
    case "/ (Divide)":
        answer = float(num1) / float(num2)
print(answer)