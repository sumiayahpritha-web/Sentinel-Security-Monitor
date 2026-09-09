print("SENTINEL SECURITY MONITOR")
print("-----------------------------")
print("system loaded successfully")
from datetime import datetime
def check_event(username, ip_address, failed_attempts):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if failed_attempts >= 5:
       print("🚨 SECURITY ALERT")
       print("Timestamp:", timestamp)
       print("username:", username)
       print("IP:", ip_address)
       print("Failed attempts:", failed_attempts)
       print("Possible brute force attack detected")

       with open("alerts.txt", "a") as alerts_file:
                  alerts_file.write(
                      f"{timestamp} | SECURITY ALERT | Username: {username} | IP Address: {ip_address} | Failed attempts: {failed_attempts} | Possible brute force attack detected\n"
                      )
              
    else:
               print("No brute force attack detected")
       

with open("events.txt","r") as file:
    events = file.readlines()
    print(events)
ip_attempts = {}


for event in events:
    username, ip_address, failed_attempts = event.strip().split(",")
    failed_attempts = int(failed_attempts)
    print("username:", username)
    print("IP:", ip_address)
    print("Failed attempts:", failed_attempts)
    check_event(username, ip_address, failed_attempts) 
    if ip_address in ip_attempts:
          ip_attempts[ip_address] += failed_attempts
    else:
          ip_attempts[ip_address] = failed_attempts
print("ACTIVITY SUMMARY")
print("____________________")

for ip_address, total_attempts in ip_attempts.items():
      print(ip_address, "_", total_attempts,"failed attempts")



       








