from pathlib import Path
from acsii_art import acsii_art
from functions import split_extension, xor_decryption, xor_encryption

print(acsii_art)

is_running = True

while is_running:
    user_select = input("Welcome. Would you like to encrypt/decrypt a TXT file or a message? (txt/msg): ").lower().strip()
    user_key = input("Enter a password between 12 and 20 characters: ").strip()
    if len(user_key) < 12 or len(user_key)> 20:
        print("Please enter a valid Password.")
    else:
        key = user_key.encode()
        if user_select == "txt":
            directory_input = input("Enter your Directory Path: ")
            directory_path = Path(directory_input)
            user_mode = input("Would you like to (e)nrypt or (d)ecrypt a message? ").lower().strip()

            #encryption
            if user_mode == "e":
                for files in directory_path.iterdir():
                    extension = split_extension(files)
                    if extension == ".txt":
                        with open(files, "r") as f:
                            text = f.read()
                        with open(files, "w") as f:
                            result = xor_encryption(text, key)
                            encrypted_file = f.write(result)
                            is_running = False

            #decryption
            if user_mode == "d":
                for files in directory_path.iterdir():
                    extension = split_extension(files)
                    if extension == ".txt":
                        with open(files, "r") as f:
                            text = f.read()
                        with open(files, "w") as f:
                            result = xor_decryption(text, key)
                            decrypted_file = f.write(result)
                            is_running = False

        if user_select == "msg":
            user_mode = input("Would you like to (e)nrypt or (d)ecrypt a message? ").lower().strip()

            #encryption
            if user_mode == "e":
                user_msg = input("Message: ").strip()
                print(xor_encryption(user_msg, key))
                is_running = False

            #decryption
            if user_mode == "d":
                user_msg = input("Message: ").strip()
                print(xor_decryption(user_msg, key))
                is_running = False