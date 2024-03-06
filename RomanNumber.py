def rimRaqam(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in s:
        curr_value = roman_dict[char]
        result += curr_value
        if curr_value > prev_value:
            result -= 2 * prev_value
        prev_value = curr_value

    return result

#
# print(rimRaqam("III"))
# print(rimRaqam("IV"))
# print(rimRaqam("XI"))
# print(rimRaqam("LVIII"))
# print(rimRaqam("MCMXCIV"))

def again():
    print("👉Read Roman Number👈")
    number = input("I = 1 , V = 5 , X = 10 , L = 50 , C = 100 , D = 500, M = 1000 👉: ")
    print(rimRaqam(number))


    back = input("""Do u want to writa another Roman number: 
        1. Yes
        2. No
            >>> """)

    if back == '1':
        return again()


    elif back == '2':
        pass

    else:
        print("Error !")
        return again()

again()