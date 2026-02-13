import json


REQUIRED_KEYS = {"userId", "id", "title", "body"}


def load_log_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def validate_schema(log_data):
    failures = []

    for entry in log_data:
        if not entry.get("success"):
            continue

        response = entry.get("response_json")

        if not isinstance(response, list):
            failures.append(entry["request_id"])
            continue

        for item in response:
            if not REQUIRED_KEYS.issubset(item.keys()):
                failures.append(entry["request_id"])
                break

    return {
        "total_requests": len(log_data),
        "schema_failures": len(failures),
        "failed_request_ids": failures
    }
