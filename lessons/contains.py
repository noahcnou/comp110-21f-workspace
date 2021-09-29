"""Example of a function that processes a list."""


def main() -> None:
    names: list(str) = ("Kris", "Kaki")
    print(contains("Kris", names))


def contains(needle: str, haystack: list(str)) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    i: int - 0
    while i < len(haystack):
        if haystack(i) == needles:
            return True
        i += 1
    return False

if __name__ == "__main__":
    main()