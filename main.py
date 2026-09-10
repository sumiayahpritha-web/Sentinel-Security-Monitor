print("SENTINEL SECURITY MONITOR")
print("-----------------------------")
print("system loaded successfully")
ip_attempts = {}
CRITICAL_THRESHOLD = 8
HIGH_THRESHOLD = 5
REPEATED_THRESHOLD = 6
total_events = 0
normal_events = 0
high_alerts = 0
critical_alerts = 0
from datetime import datetime
import time
def check_event(username, ip_address, failed_attempts):
    global total_events, normal_events, high_alerts, critical_alerts
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#making a priortity based event listing
    if failed_attempts >= CRITICAL_THRESHOLD:
       severity = "CRITICAL"
    elif failed_attempts >= HIGH_THRESHOLD:
         severity = "HIGH"
    else:
         severity = "NORMAL"
         total_events += 1
         if severity == "CRITICAL":
             critical_alerts += 1
         elif severity == "HIGH":
             high_alerts += 1
         else:
             normal_events += 1            
            
    if failed_attempts >= 5:
       print("🚨", severity,"SECURITY ALERT")
       print("Timestamp:", timestamp)
       print("username:", username)
       print("IP:", ip_address)
       print("Failed attempts:", failed_attempts)
       print("Possible brute force attack detected")

       with open("alerts.txt", "a") as alerts_file:
                  alerts_file.write(
                      f"{timestamp} | {severity} | SECURITY ALERT | Username: {username} | IP Address: {ip_address} | Failed attempts: {failed_attempts} | Possible brute force attack detected\n"
                      )
              
    else:
        print("No brute force attack detected")
    if ip_address in ip_attempts:
        ip_attempts[ip_address] += failed_attempts
    else:
        ip_attempts[ip_address] = failed_attempts
def show_report():
    print("SECURITY REPORT")
    print("___________________")
    print()
    print("TOTAL EVENTS: ",total_events)
    print("NORMAL EVENTS: ",normal_events)
    print("HIGH ALERTS: ",high_alerts)
    print("CRITICAL ALERTS: ",critical_alerts)
    print("___________________")
last_position = 0
while True:   

    with open("events.txt","r") as file:
         file.seek(last_position)
         new_events = file.readlines()
         last_position = file.tell()
          
    for event in new_events:
        if not event.strip():
             continue
        parts = event.strip().split(",")
        if len(parts) !=3:
            print("Invalid event",event.strip())
            continue
        username, ip_address, failed_attempts =parts
        try:
            failed_attempts = int(failed_attempts)
        except ValueError:
            print("invalid failed attempts",failed_attempts)
            continue

       
        print("New Events detected")
        print("username:", username)
        print("IP:", ip_address)
        print("Failed attempts:", failed_attempts)
        check_event(username, ip_address, failed_attempts) 
    if new_events: 
       print("ACTIVITY SUMMARY")
       print("____________________")

       for ip_address, total_attempts in ip_attempts.items():
           print(ip_address, "_", total_attempts,"failed attempts")
           if total_attempts >= REPEATED_THRESHOLD:
            print("REPEATED ATTACK ACTIVITY")
            print("IP:",ip_address)
            print("Total Failed Attempts:", total_attempts)
            print()
            show_report()
    time.sleep(2)  
        



       








