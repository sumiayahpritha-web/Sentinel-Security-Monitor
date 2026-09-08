print("SENTINEL SECURITY MONITOR")
print("-----------------------------")
print("system loaded successfully")

def check_event(username, ip_address, failed_attempts):
    if failed_attempts >= 5:
       print("🚨 SECURITY ALERT")
       print("username:", username)
       print("IP:", ip_address)
       print("Failed attempts:", failed_attempts)
       print("Possible brute force attack detected")

       with open("alerts.txt", "a") as alerts_file:
                  alerts_file.write(
                      f"SECURITY ALERT | Username: {username} | IP Address: {ip_address} | Failed attempts: {failed_attempts} | Possible brute force attack detected\n"
                      )
              
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
    check_event(username, ip_address, failed_attempts) 

       








