# Sentinel Security Monitor

This is a small Python project I built to learn more about how security monitoring tools actually work under the hood. It watches a log of simulated login attempts and flags stuff that looks like a brute-force attack — repeated failed logins from the same IP, that kind of thing.

I mainly wanted to get better at Python while also learning some real security concepts, so this felt like a good project to combine both.

## What it does

- Watches `events.txt` for new login attempts in real time
- Flags failed logins and sorts them by severity (normal/high/critical)
- Logs alerts to `alerts.txt` so there's a record of what happened
- Tracks stats (total events, how many were high/critical, etc.) in `statistics.txt`
- Catches bad/malformed event lines instead of crashing
- Flags IPs that keep showing up with failed attempts (possible repeated attack)

## Event format

Each line in `events.txt` looks like this:

username,IP_address,failed_attempts

Example: admin,192.168.1.20,5

## Severity levels

I set up three tiers based on how many failed attempts came in:

- **NORMAL** – under the alert threshold, nothing to worry about
- **HIGH** – hits the high threshold, worth a look
- **CRITICAL** – hits the critical threshold, likely a brute-force attempt

## Files

- `main.py` – the actual monitoring script
- `events.txt` – fake login events (this is what gets "monitored")
- `alerts.txt` – where alerts get written when something's flagged
- `statistics.txt` – running totals/stats

## Running it

```bash
python main.py

It'll keep running and checking events.txt for new lines. Ctrl+C to stop it.

Changing the thresholds
The thresholds are just variables at the top of main.py:

CRITICAL_THRESHOLD = 8
HIGH_THRESHOLD = 5
REPEATED_THRESHOLD = 6

Bump these up or down depending on how sensitive you want the alerts to be.
Why I built this
Honestly just wanted a hands-on way to practice Python while learning some basic security monitoring concepts — things like log parsing, severity classification, and detecting repeated attack patterns. Everything here uses fake/simulated data, nothing connects to a real system.
