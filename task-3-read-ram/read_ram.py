import psutil

def display_memory_usage():
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")

if __name__ == "__main__":
    display_memory_usage()
