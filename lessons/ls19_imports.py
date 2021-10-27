"""Examples of importing in Python."""


from lessons import ls19_helpers

# Alias a module / imported name as another name
from lessons import ls19_helpers as hp

# import names defined globally in a module
from lessons.ls19_helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(ls19_helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()