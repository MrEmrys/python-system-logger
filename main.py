import datetime
import time
import os
import sys

# Make sure the 'logs' directory exists
os.makedirs("logs", exist_ok=True)

LOG_FILE_PATH = "logs/.log"

try:
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        print(f"Logging started to: {LOG_FILE_PATH}")
        print("Press Ctrl+C to stop...")

        while True:
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            
            log_file.write(f"[{timestamp}] Program running\n")
            log_file.flush()  # Make sure it's written immediately
            
            time.sleep(5)

except KeyboardInterrupt:
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] Ctrl+C detected - shutting down gracefully")
    # File is auto-closed by 'with' statement

except Exception as e:
    # Catch any unexpected error
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    error_message = f"[{timestamp}] UNEXPECTED ERROR: {type(e).__name__}: {str(e)}\n"
    
    # Try to log the error even if something is wrong
    try:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(error_message)
            log_file.flush()
    except:
        print("!!! Could not write error to log file !!!")
    
    print(f"\n{error_message.strip()}")
    print("Program will exit due to unexpected error.")

finally:
    # This runs in all cases (normal exit, Ctrl+C, or exception)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Logger stopped")