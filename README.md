```
  ____       __  __          
 |  _ \ _   _\ \/ /___  _ __ 
 | |_) | | | |\  // _ \| '__|
 |  __/| |_| |/  \ (_) | |   
 |_|    \__, /_/\_\___/|_|   
        |___/                
```

**PyXor** A simple Python tool that uses the XOR cipher to encrypt and decrypt messages and text files.
-----

### About PyXor

This crypto project is for learning purposes only and not intended for production use.

**Technologies Used:** Python

PyXor is my second program exploring cryptography. I wanted to move beyond simple messages and build a tool that could encrypt and decrypt entire text files.

Here's a look at how I iterate through a directory to find and process .txt files for encryption or decryption.

```python
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
```

This snippet shows how I used the pathlib library to handle directory input, which provides better flexibility and cross-platform compatibility.

```python
        if user_select == "txt":
            directory_input = input("Enter your Directory Path: ")
            directory_path = Path(directory_input)
            user_mode = input("Would you like to (e)nrypt or (d)ecrypt a message? ").lower().strip()
```
-----

Key features and design choices:

  * **Password Validation:** A minimum password length is required to ensure a more robust encryption key.
  * **Versatile Encryption:** Encrypt and decrypt both individual messages and entire .txt files.
  * **Title Design:** The ASCII art for the title was created using [this generator](https://budavariam.github.io/asciiart-text/).
