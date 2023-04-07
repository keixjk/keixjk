# Get input from user
plaintext = input("Enter plaintext (all uppercase letters, no spaces): ")
keyword = input("Enter keyword (all uppercase letters): ")
# Function to convert keyword to numerical values
def key_to_num(keyword):
    return [ord(char) - 65 for char in keyword]
# Function to encrypt plaintext using Vigenère cipher
def encrypt(plaintext, keyword):
    # Convert keyword to numerical values
    key_num = key_to_num(keyword) 
    # Convert plaintext to numerical values
    plaintext_num = [ord(char) - 65 for char in plaintext]
    # Encrypt plaintext
    ciphertext = ""
    key_len = len(keyword)
    for i, char_num in enumerate(plaintext_num):
        key_char_num = key_num[i % key_len]
        ciphertext_char_num = (char_num + key_char_num) % 26
        ciphertext_char = chr(ciphertext_char_num + 65)
        ciphertext += ciphertext_char    
    return ciphertext
# Generate Vigenère cipher and print result
ciphertext = encrypt(plaintext, keyword)
print("Ciphertext: " + ciphertext)
