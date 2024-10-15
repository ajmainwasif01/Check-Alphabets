
def is_alphabet(char):
   
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        return True
    else:
        return False

char = input("Enter a character: ")


if is_alphabet(char):
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")
