def number_processor():

    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == "done":     #convert to lower
            break

        try:
            number = float(user_input)  # Convert input to a float
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    if count > 0:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
    else:
        print("No numbers were entered.")


number_processor()
