import pyperclip
import time

# 1. Setup
history = []
last_item = ""

print("Smart Clipboard is running... (Press Ctrl+C to stop)")

# 2. The Loop
try:
    while True:
        # Get the current content of the clipboard
        current_item = pyperclip.paste()

        # 3. The "Smart" Logic
        # Check if it's different from the last thing we saw AND not empty
        if current_item != last_item and current_item.strip() != "":
            history.insert(0, current_item) # Add to the start of the list
            last_item = current_item        # Update our "last seen" marker
            
            print(f"New snippet saved: {current_item[:30]}...")
            print(f"Total history: {len(history)} items")

        # Wait for 1 second before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping the app. Here is what you copied today:")
    for i, item in enumerate(history, 1):
        print(f"{i}: {item}")