from hello import get_hello

def get_helloworld() -> str:
    _hello = get_hello()
    return f"{_hello}"

if __name__ == "__main__":
    print(get_helloworld())
