#Function to Encrypt Text
def encrypt(text, shift1, shift2):   
    result = ""
    for ch in text:                 
        if ch.isalpha():             
            start = ord("a") if ch.islower() else ord("A")
            if 'a' <= text <= 'm':
                result += chr((ord(ch) - start + (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':
                result += chr((ord(ch) - start - (shift1 + shift2)) % 26 + start)
            elif 'A' <= text <= 'M':
                result += chr((ord(ch) - start - shift1) % 26 + start)
            elif 'N' <= text <= 'Z':
                result += chr((ord(ch) - start + (shift2**2)) % 26 + start)
        else:
            result += ch
    return result
#Function to Decrypt Text
def decrypt(text, shift1, shift2):     
    result = ""
    for ch in text:
        if ch.isalpha():
            start = ord("a") if ch.islower() else ord("A")
            if 'a' <= text <= 'm':
                result += chr((ord(ch) - start - (shift1 * shift2)) % 26 + start)
            elif 'n' <= text <= 'z':
                result += chr((ord(ch) - start + (shift1 + shift2)) % 26 + start)
            elif 'A' <= text <= 'M':
                result += chr((ord(ch) - start + shift1) % 26 + start)
            elif 'N' <= text <= 'Z':
                result += chr((ord(ch) - start - (shift2**2)) % 26 + start)
        else:
            result += ch
    return result
#Main function to run the program
def main(): 
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
#Open and Read raw_text file
    with open("raw_text.txt","r") as f:
        raw_text = f.read()
# Encrypt and save text
    encrypted_text = encrypt(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted_text)
#Run the program
if __name__ == "__main__":
    main()