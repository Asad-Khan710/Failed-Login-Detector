# Failed Login Detector

A Python-based security tool that analyzes failed login events and detects repeated authentication attempts from suspicious IP addresses within a configurable time window.

## What It Does

The program:

1. Reads failed login events from a text file.
2. Extracts timestamps, IP addresses, and usernames.
3. Validates log entries and skips malformed events.
4. Analyzes each IP address for repeated login attempts.
5. Detects the highest number of attempts within a configurable time window.
6. Assigns a severity level based on the number of attempts.
7. Generates and saves security alerts.

## Detection Logic

The detector uses two configurable values:

```python
threshold = 5
window_seconds = 60
```

By default, an IP address triggers an alert when it generates **5 or more failed login attempts within 60 seconds**.

Severity is assigned using project-defined rules:

* **MEDIUM:** 5–7 attempts
* **HIGH:** 8 or more attempts

These severity levels are specific to this project and are not intended to represent an industry-standard classification.

## Example Log

`login_events.txt` contains events in the following format:

```text
DATE TIME IP USERNAME
```

Example:

```text
2026-09-23 10:01:12 192.168.50.1 admin
2026-09-23 10:01:18 10.0.0.5 asad
2026-09-23 10:01:31 10.0.0.5 asad
2026-09-23 10:01:45 10.0.0.5 asad
```

## Example Alert

When suspicious activity is detected, the program generates an alert such as:

```text
[HIGH] 2026-09-24 12:23:38 - 10.0.0.5 - asad - 9 attempts from 2026-09-23 10:01:18 to 2026-09-23 10:02:18
```

The alert includes:

* Severity
* Detection timestamp
* Source IP address
* Targeted username
* Number of attempts
* Start of suspicious activity
* End of suspicious activity

Alerts are displayed in the terminal and saved to `alerts.txt`.

## Error Handling

The detector handles common malformed log entries without stopping the entire analysis.

Invalid entries are skipped when:

* Required fields are missing.
* The timestamp cannot be parsed.

The program also reports the number of valid and invalid events processed.

## Project Structure

```text
Failed-Login-Detector/
│
├── login_detector.py
├── login_events.txt
├── alerts.txt
└── README.md
```

`alerts.txt` contains generated alerts and is intended to be treated as runtime output rather than source code.

## How It Works

The program first reads and validates each event from `login_events.txt`.

Each valid event is stored with its:

* Timestamp
* IP address
* Username

The program then groups events by IP address and examines each possible time window.

For each starting event, later events are compared against the configured time window. The detector keeps track of the window containing the highest number of attempts.

If the highest count reaches the configured threshold, an alert is generated.

## Skills Demonstrated

* Python
* File handling
* Dictionaries
* Lists
* Loops
* Conditional statements
* Exception handling
* `datetime` and timestamp processing
* String parsing
* Structured data handling
* Time-window analysis
* Security event analysis
* Alert generation
* Basic log analysis

## Future Improvements

Potential future improvements include:

* Support for real authentication logs such as Linux or Windows event logs
* Command-line arguments for configuring detection thresholds
* Additional authentication attack detection
* More detailed alert reporting
* Exporting alerts in structured formats such as JSON
* Integration with a larger security monitoring or SIEM environment

## Purpose

This project was created as a practical cybersecurity exercise to develop Python scripting skills and apply them to security event analysis.

The project focuses on a common security monitoring scenario: identifying repeated failed authentication attempts that may indicate password spraying, brute-force activity, or other suspicious authentication behavior.
