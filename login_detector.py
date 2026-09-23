login_events = []

# Read login events from the file
try:
    with open("login_events.txt", "r") as file:
        for line in file:
            login_events.append(line.strip())

except FileNotFoundError:
    print("Error: login_events.txt was not found")


failed_logins = {}

threshold = 5


# Check whether an IP has reached the alert threshold
def analyze_ip(ip, attempts):
    if attempts >= threshold:
        return "ALERT", attempts
    else:
        return "NORMAL", attempts


# Count failed login attempts for each IP
for ip in login_events:

    if ip not in failed_logins:
        failed_logins[ip] = 0

    failed_logins[ip] += 1


# Analyze and display each IP
for ip in failed_logins:

    status, attempts = analyze_ip(ip, failed_logins[ip])

    print(status, ip, "-", attempts, "failed attempts")