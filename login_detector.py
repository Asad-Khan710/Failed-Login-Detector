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

    event1 = login_events[0]
    event2 = login_events[1]

    difference = event2["timestamp"] - event1["timestamp"]
    seconds = difference.total_seconds()
    print(seconds)

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