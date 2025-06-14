def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # keep non-alphabetic characters unchanged
    return result

def main():
    print("🔐 Caesar Cipher - Encrypt or Decrypt")
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Shift must be between 0 and 25.")
        except ValueError:
            print("Please enter a valid number.")

    mode = ''
    while mode not in ['encrypt', 'decrypt']:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode.title()}ed): {output}")

if __name__ == "__main__":
    main()
