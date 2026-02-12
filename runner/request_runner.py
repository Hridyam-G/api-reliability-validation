import requests
import time
import json
from datetime import datetime


API_URL = "https://jsonplaceholder.typicode.com/posts"
NUM_REQUESTS = 20
TIMEOUT_SECONDS = 5


def run_requests():
    results = []

    for i in range(NUM_REQUESTS):
        start_time = time.time()

        try:
            response = requests.get(API_URL, timeout=TIMEOUT_SECONDS)
            latency = time.time() - start_time

            result = {
                "request_id": i,
                "status_code": response.status_code,
                "latency_seconds": latency,
                "success": response.status_code == 200,
                "response_size_bytes": len(response.content),
                "response_json": response.json()
            }

        except requests.exceptions.RequestException as e:
            latency = time.time() - start_time

            result = {
                "request_id": i,
                "status_code": None,
                "latency_seconds": latency,
                "success": False,
                "error": str(e)
            }

        results.append(result)

    return results


def save_results(results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs/run_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Saved results to {filename}")


if __name__ == "__main__":
    data = run_requests()
    save_results(data)
