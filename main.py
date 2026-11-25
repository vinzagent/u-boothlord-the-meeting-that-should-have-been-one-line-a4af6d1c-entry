import os
import sys

ENTRY = "It's approved, it's due Friday, and it's all in the email from this morning that nobody opened."

def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod("/output/entry.txt", 0o644)
    except OSError:
        pass
    sys.stdout.write(ENTRY)

if __name__ == "__main__":
    main()
