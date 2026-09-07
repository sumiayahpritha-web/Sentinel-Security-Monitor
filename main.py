print("SENTINEL SECURITY MONITOR")
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


with open("events.txt","r") as file:
    events = file.readlines()
    print(events)
for event in events:
    username, ip_address, failed_attempts = event.strip().split(",")
    failed_attempts = int(failed_attempts)
    print("username:", username)
    print("IP:", ip_address)
    print("Failed attempts:", failed_attempts)

    if failed_attempts >= 5:
       print("Possible brute force attack detected")
    else:
       print("No brute force attack detected")









