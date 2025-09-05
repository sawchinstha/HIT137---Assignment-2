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
            elif 'A' <= ch <= 'M':  # For lowercase 'a' to 'm'
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
            elif 'A' <= ch <= 'M':
                result += chr((ord(ch) - start + shift1) % 26 + start)
            elif 'N' <= text <= 'Z':
                result += chr((ord(ch) - start - (shift2**2)) % 26 + start)
        else:
            result += ch  # Non-alphabetic characters are left unchanged
    return result

# Main function to run the encryption/decryption process
def main():
    # Take shift values from user with validation
    shift1 = int(input("Enter  shift 1 (integer): "))
    shift2 = int(input("Enter shift 2 (integer): "))

    # Open and Read raw_text file
    try:
        with open("raw_text.txt", "r") as f:
            raw_text = f.read()  # Read the original text
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")  # Handle missing file
        return

    # Encrypt and save text
    encrypted_text = encrypt(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)  # Save encrypted text

    # Read the Encrypted Text
    with open("encrypted_text.txt", "r") as f:
        encrypted_message = f.read()  # Read back encrypted text

    # Decrypt and save text
    decrypted_text = decrypt(encrypted_message, shift1, shift2)
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted_text)  # Save decrypted text

    # Compare raw and decrypted text
    if raw_text == decrypted_text:
        print("Decryption Successful")  # Successful decryption
    else:
        print("Decryption Failed")  # Decryption mismatch

# Run the program
if __name__ == "__main__":
    main()  # Call main function


