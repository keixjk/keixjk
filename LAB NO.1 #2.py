# prompt the user for input
encrypted_text = input("Enter a string to decrypt: ")
def decrypt_string(encrypted_text):
    decrypted_text = "\033[1;32m"

# check every character
    for char in encrypted_text:
# if *, change to a
        if char == "*":
            decrypted_text += "a"
# if &, change to e      
        elif char == "&":
            decrypted_text += "e"
# if #, change to i
        elif char == "#":
            decrypted_text += "i"
# if +, change to o
        elif char == "+":
            decrypted_text += "o"
# if !, change to u
        elif char == "!":
            decrypted_text += "u"
        else:
            decrypted_text += char
    return decrypted_text

# print output
plain_text = decrypt_string(encrypted_text)
print(plain_text)
