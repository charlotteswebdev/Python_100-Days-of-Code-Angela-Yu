alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = [letter.upper() for letter in alphabet_lower]

def decode(start_text, shift_amount):
    end_text = ""
    shift_amount += 1
    for char in start_text:
        if char in alphabet_lower:
            position = alphabet_lower.index(char)
            new_position = (position + shift_amount) % len(alphabet_lower)
            end_text += alphabet_lower[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position + shift_amount) % len(alphabet_upper)
            end_text += alphabet_upper[new_position]
        else:
            end_text += char
    return end_text

start_text = input("Enter the start text: ")
print("\nAll possible variations:")
for shift in range(26):
    print(f"Shift {shift}: {decode(start_text, shift)}")
