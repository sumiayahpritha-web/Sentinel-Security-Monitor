print("SENTINAL SECURITY MONITOR")
print("-----------------------------")
print("system loaded successfully")
username = "admin"
ip_address = "192.168.1.20"
failed_attempts = 7
print(username)
print(ip_address)
print(failed_attempts)
if failed_attempts >= 5:
    print("Possible brute force attack detected")
else:
    print("No brute force attack detected")
username = input("Enter name: ")
ip_address = input("Ip address: ")
failed_attempts = int(input("Enter Failed attempts : "))
    





