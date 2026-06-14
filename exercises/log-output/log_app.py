import time
import uuid
from datetime import datetime, timezone


unique_id = str(uuid.uuid4())


def log_message():
    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    log_entry = f"{timestamp}: {unique_id}"
    print(log_entry, flush=True)


if __name__ == "__main__":
    while True:
        log_message()
        time.sleep(5)