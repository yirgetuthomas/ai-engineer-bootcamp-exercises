"""Study report: how many minutes did I spend on each topic?

Run it from the top folder of the repository:
    python session-04/round_1/study_report.py
"""

import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "study_log.json"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def load_sessions():
    """Read the study log: a list of sessions, each with a topic, a start and an end."""
    with open(LOG_FILE) as file:
        return json.load(file)


def minutes_studied(session):
    """Work out how long one session lasted, in minutes."""
    start = datetime.strptime(session["start"], TIME_FORMAT)
    end = datetime.strptime(session["end"], TIME_FORMAT)
    return (end - start).total_seconds() / 60


def build_report(sessions):
    """Add up the minutes for each topic."""
    totals = {}
    for session in sessions:
        topic = session["topic"]
        totals[topic] = totals.get(topic, 0) + minutes_studied(session)
    return totals


def main():
    totals = build_report(load_sessions())
    for topic, minutes in totals.items():
        print(f"{topic}: {minutes:.0f} minutes")
    print(f"Total: {sum(totals.values()):.0f} minutes")


if __name__ == "__main__":
    main()
