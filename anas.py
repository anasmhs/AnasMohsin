import hashlib

# String to hash by Anas Al-Harrasi
#MD5 Hash 

StringData = input("Type the string that you want to convert to MD5:")
result = hashlib.md5(StringData.encode())
print("The MD5 of your sting data is : ")
print(result.hexdigest())

