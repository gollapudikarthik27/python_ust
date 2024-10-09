MAX_SIZE = 5

# Initialize the queue and the current index
queue = {}
current_index = 0

# Adding items in a loop
for i in range(1, 10):  # Adding more than 5 items to test the circular behavior
    key = f"key{i}"
    value = i

    if len(queue) < MAX_SIZE:
        # Add item if queue is not full
        queue[key] = value
    else:
        # Delete the latest added element
        latest_key = list(queue.keys())[current_index]
        del queue[latest_key]
        # Add the new item
        queue[key] = value

    # Update the circular index
    current_index = (current_index + 1) % MAX_SIZE

    print(f"After adding {key}: {queue}")
