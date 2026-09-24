from datetime import datetime

login_events = []
failed_logins = {}

threshold = 5


def analyze_ip(ip, attempts):
    if attempts >= threshold:
        return "ALERT", attempts
    else:
        return "NORMAL", attempts


try:
    with open("login_events.txt", "r") as file:
        for line in file:
            parts = line.split()

            timestamp = parts[0] + " " + parts[1]
            event_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

            event = {
                "timestamp": event_time,
                "ip": parts[2]
            }

            login_events.append(event)

except FileNotFoundError:
    print("Error: login_events.txt was not found")


for event in login_events:
    ip = event["ip"]

    if ip not in failed_logins:
        failed_logins[ip] = 0

    failed_logins[ip] += 1


for ip in failed_logins:
    status, attempts = analyze_ip(ip, failed_logins[ip])
    print(status, ip, "-", attempts, "failed attempts")

    ip_events = []

    for event in login_events:
        if event["ip"] == ip:
            ip_events.append(event)


    for i in range(len(ip_events)):
        count = 1

        for j in range(i + 1, len(ip_events)):
            difference = ip_events[j]["timestamp"] - ip_events[i]["timestamp"]
            seconds = difference.total_seconds()

            if seconds <= 60:
                count += 1
            else:
                break

        if count >= threshold:
            print("ALERT:", ip, "-", count, "attempts within 60 seconds")
            break