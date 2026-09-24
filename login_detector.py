from datetime import datetime

login_events = []
failed_logins = {}
invalid_lines = 0

threshold = 5
window_seconds = 60


# Read and process login events from the log file
try:
    with open("login_events.txt", "r") as file:
        for line in file:
            parts = line.split()

            if len(parts) < 4:
                invalid_lines += 1
                continue

            timestamp = parts[0] + " " + parts[1]

            try:
                event_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                invalid_lines += 1
                continue

            event = {
                "timestamp": event_time,
                "ip": parts[2],
                "username": parts[3]
            }

            login_events.append(event)

except FileNotFoundError:
    print("Error: login_events.txt was not found")


for event in login_events:
    ip = event["ip"]

    if ip not in failed_logins:
        failed_logins[ip] = 0

    failed_logins[ip] += 1


# Analyze each IP address for repeated login attempts
with open("alerts.txt", "a") as alert_file:
    for ip in failed_logins:
        ip_events = []

        for event in login_events:
            if event["ip"] == ip:
                ip_events.append(event)

        highest_count = 0
        start_time = None
        end_time = None
        username = None

        # Check each event at the start of a time window
        for i in range(len(ip_events)):
            count = 1
            current_end_time = ip_events[i]["timestamp"]

            # Compare the current event with later
            for j in range(i + 1, len(ip_events)):
                difference = ip_events[j]["timestamp"] - ip_events[i]["timestamp"]
                seconds = difference.total_seconds()

                # Count attempts that within time window
                if seconds <= window_seconds:
                    count += 1
                    current_end_time = ip_events[j]["timestamp"]
                else:
                    break

            if count > highest_count:
                highest_count = count
                start_time = ip_events[i]["timestamp"]
                end_time = current_end_time
                username = ip_events[i]["username"]

        if highest_count >= threshold:

            alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if highest_count >= 8:
                severity = "HIGH"
            else:
                severity = "MEDIUM"

            alert_message = f"[{severity}] {alert_time} - {ip} - {username} - {highest_count} attempts from {start_time} to {end_time}"

            print(alert_message)
            alert_file.write(alert_message + "\n")


print(f"Processed {len(login_events)} valid events")
print(f"Skipped {invalid_lines} invalid lines")