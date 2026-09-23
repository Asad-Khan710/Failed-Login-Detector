# Failed Login Detector

A simple Python-based security tool that analyzes failed login events and identifies IP addresses that exceed a defined number of failed attempts.

## What It Does

The program:

1. Reads failed login events from a text file.
2. Counts the number of failed attempts for each IP address.
3. Compares each IP against a configured threshold.
4. Generates an alert when an IP reaches or exceeds the threshold.

## Example

If an IP address generates 5 or more failed login attempts, the program reports it as an alert.

Example output:

```text
NORMAL 192.168.50.1 - 3 failed attempts
ALERT 10.0.0.5 - 6 failed attempts
NORMAL 192.168.50.2 - 1 failed attempts
NORMAL 172.16.0.20 - 1 failed attempts
```

In this example, `10.0.0.5` generated 6 failed login attempts and exceeded the alert threshold.

## Project Structure

```text
failed-login-detector/
├── login_detector.py
├── login_events.txt
└── README.md
```

## How It Works

The program reads each line from `login_events.txt` and stores the IP addresses.

It then counts how many times each IP appears in the file.

Each IP is passed to a function that determines whether its number of failed attempts has reached the threshold.

## Skills Demonstrated

* Python
* File handling
* Dictionaries
* Lists
* Loops
* Functions
* Conditional statements
* Exception handling
* Basic security event analysis

## Future Improvements

Possible future improvements include:

* Reading real authentication logs
* Including timestamps
* Detecting repeated attempts within a specific time period
* Logging alerts to a separate file
* Adding command-line arguments
* Detecting multiple types of suspicious activity

## Purpose

This project was created as a practical cybersecurity exercise to develop Python scripting skills and explore how security tools can analyze authentication events.
