"""Get loopy."""


def up(haystack: str, needle: str) -> int:
    print("up")
    i: int = 0
    count: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            count = count + 1
        i = i + 1
    return count