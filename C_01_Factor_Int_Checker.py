# Ask user for widht and loop untill they enter a number that is more than zero

def num_check (question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

      
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # asking for input
            response = int(response)

            # checking that the num is > 0
            if 1 <= response <= 200:
                return response
            else:
                print("error")

      
        except ValueError:
            print(error)

# Main Routine Here
while True:
    to_factor = num_check("To Factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
