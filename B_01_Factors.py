# Genarates headings (eg: --- Header ---)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions if requested
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc
    ''')


# Ask for integer between 1 and 200.
def num_check (question):

    error = "Please enter a number that is between 1 and 200\n"
    while True:

        try:
            # asking for input
            response = float(input(question))

            # checking that the num is between 1 and 100 inclusive
            if 1 <= to_factor <= 200:
                return response
            else:
                print("error")

        except ValueError:
            print(error)


# Works out factors, returns sorted list
def factor(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
        num = num/divisor
# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# displays instructions if requested
want_instructions = input("\nPress <enter> to read instructions"
                          " or any key to continue")
if want_instructions == "":
    instructions()

while True:
    comment = ""

    # ask user for number to be factorizsed
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself."

    # comments for squares / primes
        
    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number."

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a prefect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comments
    print()    
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("\nThanks for using the The Ultimate Factor Finder!")
