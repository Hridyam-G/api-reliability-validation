from validator.schema_validator import load_log_file, validate_schema
from validator.latency_validator import validate_latency


LOG_FILE = "logs/<latest_log_file>.json"


def run_validation():
    data = load_log_file(LOG_FILE)

    schema_result = validate_schema(data)
    latency_result = validate_latency(data)

    print("Schema Validation:", schema_result)
    print("Latency Validation:", latency_result)


if __name__ == "__main__":
    run_validation()
