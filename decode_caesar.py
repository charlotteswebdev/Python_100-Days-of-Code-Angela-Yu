alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = [letter.upper() for letter in alphabet_lower]

def shift_text(text, shift_amount):
    result = ""
    for char in text:
        if char in alphabet_lower:
            position = alphabet_lower.index(char)
            new_position = (position + shift_amount) % len(alphabet_lower)
            result += alphabet_lower[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position + shift_amount) % len(alphabet_upper)
            result += alphabet_upper[new_position]
        else:
            result += char
    return result

def encode(text, shift_amount):
    # Encoding shifts characters forward
    return shift_text(text, shift_amount)

def decode(text, shift_amount):
    # Decoding shifts characters backward
    return shift_text(text, -shift_amount)

start_text = input("Enter the start text: ")
shift_amount = int(input("Enter the shift amount (positive for forward, negative for backward): "))

encoded_text = encode(start_text, shift_amount)
decoded_text = decode(encoded_text, shift_amount)

print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")
