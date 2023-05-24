# This is a sample Python script.
def string_function(string):
    try:
        int(string)
        return True
    except ValueError:
        try:
            complex(string)
            return True
        except ValueError:
            return False

 # // to find with the input string

str = input("enter the string:")
if string_function(str):
    print("valid")
else:
    print("not valid")

# provided test cases.

test_cases = ["0","0.1 ","1e10","2E-5","-10e3","abc","5e","+-2","e7",]

# other test cases.

test_cases = ["12.54.1","-3.14","3-2j","-32e","10."]

for case in test_cases:
    result = string_function(case)
    print(f"{case}: {result}")

