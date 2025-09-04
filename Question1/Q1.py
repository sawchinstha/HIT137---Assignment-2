# Function to encrypt text using custom shifting logic
def encrypt(text, shift1, shift2):   
    result = "" # Initialize empty string to store encrypted text
    for ch in text:                 
        if ch.isalpha(): # Only encrypt alphabetic characters            
            start = ord("a") if ch.islower() else ord("A")  # Determine ASCII start for lowercase or uppercase
            
             # Custom encryption logic based on character range
            if 'a' <= ch <= 'm':
                result += chr((ord(ch) - start + (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':  # For lowercase 'n' to 'z'
                result += chr((ord(ch) - start - (shift1 + shift2)) % 26 + start)
            elif 'a' <= ch <= 'm':  # For lowercase 'a' to 'm'
                result += chr((ord(ch) - start - shift1) % 26 + start)
            elif 'N' <= text <= 'Z':  # For Uppercase 'N' to 'Z'
                result += chr((ord(ch) - start + (shift2**2)) % 26 + start)
        else:
            result += ch  # Non-alphabetic characters are left unchanged
    return result
# Function to decrypt text using the reverse of the encryption logic
def decrypt(text, shift1, shift2):     
    result = "" # Initialize empty string to store decrypted text
    for ch in text:
        if ch.isalpha(): # Only decrypt alphabetic characters
            start = ord("a") if ch.islower() else ord("A")  # Determine ASCII start

            # Reverse the encryption logic based on character range
            if 'a' <= ch <= 'm':
                result += chr((ord(ch) - start - (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':
                result += chr((ord(ch) - start + (shift1 + shift2)) % 26 + start)
            elif 'a' <= ch <= 'm':
                result += chr((ord(ch) - start + shift1) % 26 + start)
            elif 'N' <= text <= 'Z':
                result += chr((ord(ch) - start - (shift2**2)) % 26 + start)
        else:
            result += ch  # Non-alphabetic characters are left unchanged
    return result
# Main function to run the encryption/decryption process
def main(): 
     # Take shift values from user
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
#Open and Read raw_text file
    with open("raw_text.txt","r") as f:
        raw_text = f.read()
#Encrypt and save text
    encrypted_text = encrypt(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)
#Read the Encrypted Text
    with open("encrypted_text.txt","r") as f:
        encrypted_message = f.read()
#Decrypt and save text
    decrypted_text = decrypt(encrypted_message, shift1, shift2)
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)
#Compare raw and decrypted tex
    if raw_text == decrypted_text:
        print("Decryption Successfull")
    else:
        print("Decryption Failed")   
#Run the program
if __name__ == "__main__":
    main()
#End
# Function to encrypt text using custom shifting logic
def encrypt(text, shift1, shift2):   
    result = "" # Initialize empty string to store encrypted text
    for ch in text:                 
        if ch.isalpha(): # Only encrypt alphabetic characters            
            start = ord("a") if ch.islower() else ord("A")  # Determine ASCII start for lowercase or uppercase
            
             # Custom encryption logic based on character range
            if 'a' <= ch <= 'm':
                result += chr((ord(ch) - start + (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':  # For lowercase 'n' to 'z'
                result += chr((ord(ch) - start - (shift1 + shift2)) % 26 + start)
            elif 'a' <= ch <= 'm':  # For lowercase 'a' to 'm'
                result += chr((ord(ch) - start - shift1) % 26 + start)
            elif 'N' <= text <= 'Z':  # For Uppercase 'N' to 'Z'
                result += chr((ord(ch) - start + (shift2**2)) % 26 + start)
        else:
            result += ch  # Non-alphabetic characters are left unchanged
    return result
# Function to decrypt text using the reverse of the encryption logic
def decrypt(text, shift1, shift2):     
    result = "" # Initialize empty string to store decrypted text
    for ch in text:
        if ch.isalpha(): # Only decrypt alphabetic characters
            start = ord("a") if ch.islower() else ord("A")  # Determine ASCII start

            # Reverse the encryption logic based on character range
            if 'a' <= ch <= 'm':
                result += chr((ord(ch) - start - (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':
                result += chr((ord(ch) - start + (shift1 + shift2)) % 26 + start)
            elif 'a' <= ch <= 'm':
                result += chr((ord(ch) - start + shift1) % 26 + start)
            elif 'N' <= text <= 'Z':
                result += chr((ord(ch) - start - (shift2**2)) % 26 + start)
        else:
            result += ch  # Non-alphabetic characters are left unchanged
    return result
# Main function to run the encryption/decryption process
def main(): 
     # Take shift values from user
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
#Open and Read raw_text file
    with open("raw_text.txt","r") as f:
        raw_text = f.read()
#Encrypt and save text
    encrypted_text = encrypt(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)
#Read the Encrypted Text
    with open("encrypted_text.txt","r") as f:
        encrypted_message = f.read()
#Decrypt and save text
    decrypted_text = decrypt(encrypted_message, shift1, shift2)
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)
#Compare raw and decrypted tex
    if raw_text == decrypted_text:
        print("Decryption Successfull")
    else:
        print("Decryption Failed")   
#Run the program
if __name__ == "__main__":
    main()
#End
