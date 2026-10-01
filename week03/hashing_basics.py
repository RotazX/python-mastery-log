import hashlib

def sha256_hex_string(text: str) -> str:
    b_text = text.encode()
    text = hashlib.sha256(b_text)
    return text.hexdigest()

def md5_hex_string(text: str) -> str:
    b_text = text.encode()
    text = hashlib.md5(b_text)
    return text.hexdigest()

def sha256_hex_file(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_content = f.read()
        hasher = hashlib.sha256(file_content)
        return hasher.hexdigest()

def md5_hex_file(file_path: str) -> str:
    with open(file_path, "rb") as f:
            file_content = f.read()
            hasher = hashlib.md5(file_content)
            return hasher.hexdigest()

if __name__ == "__main__":

    print(sha256_hex_string("hello"))
    if sha256_hex_string("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855":
        print("True")
    else:   
        print("They are not the same.")

    if md5_hex_string("hello") == "5d41402abc4b2a76b9719d911017c592":
        print("Hex True")
    else:
        print("They are not the same.")
    if md5_hex_string("") == "d41d8cd98f00b204e9800998ecf8427e":
        print("Hex true")
    else:
        print("Hex is wrong.")

    if sha256_hex_file("hello.txt") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824":
        print("True")
    else:
        print("HEx is wrong.")
    if md5_hex_file("hello.txt") == "5d41402abc4b2a76b9719d911017c592":
            print("Hex True")
    else:
        print("They are not the same.")
    
