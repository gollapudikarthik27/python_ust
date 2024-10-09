import threading
import re


def passwd_create(input1, pattern):
    if 6 <= len(input1) <= 12:
        out = re.search(pattern, input1)
        if out:
            print(f"Valid password found: {out.group()}")


def thread_function(input1, pattern):
    passwd_create(input1, pattern)


if __name__ == "__main__":
    pattern = r"[A-Z]{1}[a-z]{1,4}\d+[$#@]{1}\d{1}"

    inputs = [
        "Aabc12$3",
        "Bdef34#5",
        "Cghi56@7",
        "InvalidPassword123",
        "Short1$",
        "LongPassword123#",
        "Axy12@2"
    ]

    threads = []

    for user_input in inputs:
        thread = threading.Thread(target=thread_function, args=(user_input, pattern))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print("Password validation complete.")
