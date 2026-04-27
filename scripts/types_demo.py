#!/usr/bin/env python3

def main():
    integer_value = 10
    float_value = 3.14
    name = "Alice"
    greeting = "Hello"

    print("Integer:", integer_value, "type:", type(integer_value).__name__)
    print("Float:", float_value, "type:", type(float_value).__name__)

    sum_result = integer_value + float_value
    print("Arithmetic: integer + float =", sum_result, "type:", type(sum_result).__name__)
    print("Arithmetic: integer * 2 =", integer_value * 2)
    print("Arithmetic: integer / 3 =", integer_value / 3)
    print("Arithmetic: integer // 3 =", integer_value // 3)

    concatenated = greeting + ", " + name + "!"
    formatted = f"{greeting}, {name}. You have {integer_value} items."
    print("String concatenation:", concatenated)
    print("Formatted string:", formatted)

    str_number = "5"
    try:
        print("Type mismatch example (int + str):", integer_value + str_number)
    except TypeError as e:
        print("Caught TypeError as expected:", e)

    print("After conversion: integer + int('5') =", integer_value + int(str_number))
    print("After conversion: str(integer) + '5' =", str(integer_value) + str_number)

    float_str = "3.7"
    print("int(float('3.7')) =", int(float(float_str)))
    print("int(float_value) (truncation) =", int(float_value))


if __name__ == "__main__":
    main()
