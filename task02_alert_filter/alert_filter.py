
import json
import sys


def load_events(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_critical(events):
    return [
        event
        for event in events
        if event.get("level") == "critical"
    ]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "events.json"

    events = load_events(path)
    critical_events = filter_critical(events)

    for event in critical_events:
        print(event["msg"])

    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()