# Lab 4 - Iterator, mediator and interpreter*

class Context:
    def __init__(self, input_roman):
        self.input = input_roman
        self.output = 0

class Expression:
    def interpret(self, context: Context):
        for roman, value in self.roman_numerals().items():
            while context.input.startswith(roman):
                context.output += value
                context.input = context.input[len(roman):]

    def roman_numerals(self):
        return {}

class ThousandExpression(Expression):
    def roman_numerals(self):
        return {"M": 1000}

class HundredExpression(Expression):
    def roman_numerals(self):
        return {
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100
        }

class TenExpression(Expression):
    def roman_numerals(self):
        return {
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10
        }

class OneExpression(Expression):
    def roman_numerals(self):
        return {
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

# === Інтерпретатор ===
def interpret_roman(roman: str) -> int:
    context = Context(roman)
    tree = [
        ThousandExpression(),
        HundredExpression(),
        TenExpression(),
        OneExpression()
    ]
    for expr in tree:
        expr.interpret(context)
    return context.output


roman_numbers = ["XIV", "XLII", "MCMXCIV", "LXX", "IX"]
for roman in roman_numbers:
    arabic = interpret_roman(roman)
    print(f"{roman} = {arabic}")