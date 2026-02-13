def validate_latency(log_data, max_avg_latency=0.5):
    latencies = [
        entry["latency_seconds"]
        for entry in log_data
        if entry.get("success")
    ]

    if not latencies:
        return {
            "average_latency": None,
            "max_latency": None,
            "passed": False
        }

    avg_latency = sum(latencies) / len(latencies)
    max_latency = max(latencies)

    return {
        "average_latency": avg_latency,
        "max_latency": max_latency,
        "passed": avg_latency <= max_avg_latency
    }
