import secrets

count = int(input("Enter the desired password length: "))

if count <= 0:
    print("Invalid input,Enter a positive number.")
    exit()

allowed_chars = "@!#&$*abcdefghijklmnoABCDEFGHIJKLMpqrstuvwxyzNOPQRSTUVWXYZ"

key = "".join(secrets.choice(allowed_chars)
           for i in range(count))

print("Your Password is generated:",key)
