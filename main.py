import json

def calculator(i3, i1, i2, data):
    a = data[i1]
    b = data[i2]
    result = i3 * (b / a)
    return result

def main():
    print("---------CURRENCY CONVERTOR----------")

    with open('data.json', 'r') as file:
        data = json.load(file)

    while True:
        print("\nAvailable currencies:")
        print(", ".join(sorted(data.keys())))

        print("\nConvert from:______, Convert to:_______    | EX:  USD,INR   ")
        try:
            i1, i2 = map(str.strip, input().split(","))
        except ValueError:
            print("Please enter two currencies separated by a comma (e.g., USD,INR)")
            continue

        if i1 not in data or i2 not in data:
            print("One or both currencies not found.")
            continue
        if i1 == i2:
            print("Enter two different currencies.")
            continue

        while True:
            while True:
                try:
                    i3 = float(input("Amount: "))
                    break  # valid amount entered, exit this loop
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")

            result = calculator(i3, i1, i2, data)
            print(f"{i3} {i1} = {round(result, 2)} {i2}")

            print("\nPress:")
            print("1. Convert again with same currencies")
            print("2. Change currencies")
            print("3. Exit")

            # Here is the added loop for validating choice input:
            while True:
                check = input("Your choice: ")
                if check in ['1', '2', '3']:
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")

            if check == '1':
                continue  # convert again with same currencies
            elif check == '2':
                break  # change currencies (go back to outer loop)
            elif check == '3':
                print("Exiting Currency Converter.")
                return

if __name__ == "__main__":
    main()
