def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def sing(starting_number):
    bottles = starting_number
    while bottles > 0:
        if bottles > 1:
            next_bottles = bottles - 1
            if next_bottles == 1:
                next_line = "1 bottle of beer on the wall."
            else:
                next_line = f"{next_bottles} bottles of beer on the wall."
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {next_line}")
            print()
        elif bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        bottles -= 1
