
# Simple Cybersecurity System Check Tool
# Created by Nompumelelo Zulu

print("=== Security System Check ===")

username = input("Enter your username: ")
password = input("Enter your password: ")

if password == "Admin123":
    print("Access granted. System secure.")
else:
    print("Warning! Incorrect password. Possible intrusion attempt.")
