# Solution to 16. Caesar cipher

def encrypt(text, shift):
    """Shift every letter forward by `shift` places, keeping case and leaving other characters alone."""
    result = ""
    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
        elif "A" <= char <= "Z":
            base = ord("A")
        else:
            result += char
            continue
        position = ord(char) - base
        result += chr((position + shift) % 26 + base)
    return result


def decrypt(text, shift):
    """Undo encrypt()."""
    return encrypt(text, -shift)
