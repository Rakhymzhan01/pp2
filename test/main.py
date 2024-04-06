import time

def create_files():
    count = 1
    while True:
        file_name = f"{count}.txt"
        with open(file_name, 'w') as file:
            file.write("Hello, this is file " + str(count))
        print(f"Created file: {file_name}")
        count += 1
        time.sleep(1)

try:
    create_files()
except KeyboardInterrupt:
    print("Program stopped by user.")
