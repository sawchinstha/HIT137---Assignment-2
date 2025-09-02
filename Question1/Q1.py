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
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

with open("raw_text.txt","r") as f:
        raw_text = f.read()