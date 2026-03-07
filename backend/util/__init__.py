import time
from typing import Callable, List, Any
import os


def timer(func: Callable, args: List[Any]):
    start = time.time()

    response = func(*args)

    end = time.time()
    print(f"🕒 Time taken: {end - start:.2f} seconds")

    return response


def read_file(file_path: str) -> str | None:
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        return f.read()


def write_file(content: str, file_path: str):
    with open(file_path, "w") as f:
        return f.write(content)
