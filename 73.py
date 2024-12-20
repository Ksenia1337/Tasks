phrase = input("Введите фразу для шифрования: ") 
shift = int(input("Введите количество символов для сдвига: ")) 
def caesarcipher(phrase, shift): 
    result = "" 
    for char in phrase: 
        if char.isalpha(): 
            if char.islower(): 
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) 
            elif char.isupper(): 
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) 
        else: 
            result += char 
    return result 
encryptedphrase = caesarcipher(phrase, shift) 
print("Зашифрованная фраза:", encryptedphrase)