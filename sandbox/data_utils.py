"""Utility Functions."""

__author__ = "730408365"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV file line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oreinted table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(c_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` (a parameter) rows of data for each column."""
    empty_dict: dict[str, list[str]] = {}
    for keys in c_table:
        empty_list: list[str] = []
        a: int = 0
        while rows > len(c_table):
            rows = len(c_table)
        while a < rows:
            empty_list.append(c_table[keys][a])
            a += 1
        empty_dict[keys] = empty_list
    return empty_dict


def select(c_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    empty_list: dict[str, list[str]] = {}
    for keys in names:
        x = c_table[keys]
        empty_list[keys] = x
    return empty_list
 

def concat(c_table: dict[str, list[str]], c_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    empty_list: dict[str, list[str]] = {}
    for keys in c_table:
        x = c_table[keys]
        empty_list[keys] = x
    for keys in c_table_2:
        if keys in empty_list:
            y = c_table_2[keys]
            empty_list[keys] += y
        else:
            x = c_table_2[keys]
            empty_list[keys] = x
    return empty_list


def count(count_item: list[str]) -> dict[str, int]:
    """Counts appearances of word and lists in dictionary."""
    new_dict: dict[str, int] = {}
    i: int = 0
    if i < len(count_item):
        a: int = 1
        b: int = 0
        while b < len(count_item):
            if b != 1:
                if count_item[b] == count_item[i]:
                    a += 1
            b += 1
        new_dict[count_item[i]] = a
        i += 1
    return new_dict


def masked(col: list[float], mask: list[bool]) -> list[float]:
    result: list[float] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


def less_than(col: list[float], threshold: float) -> list[bool]:
    result: list[bool] = []
    for item in col:
        result.append(item < threshold)
    return result


def is_synch(column: dict[str, list[str]]) -> list[bool]:
    """Converts the column into yes or no values to more easily read data."""
    result: list[bool] = []
    returned: list[str] = column['section']
    for value in returned:
        if value == "In-Person":
            result.append(True)
        else:
            result.append(False)
    return result


def is_apa(column: dict[str, list[str]]) -> list[bool]:
    """Converts the values found in the AP_A column into a usable list of boolean values."""
    result: list[bool] = []
    returned: list[str] = column['AP_A']
    for value in returned:
        if value == 'Yes':
            result.append(True)
        else:
            result.append(False)
    return result


def apa_in_sync(apa: list[bool], sync: list[bool]) -> dict[str, int]:
    """Counts the number of students in the APA category who are enrolled in Kris Jordan's sync lectures."""
    result: dict[str, int] = {}
    n: int = 0
    o: int = 0
    a: int = 0
    for i in range(len(sync)):
        if apa[i] and sync[i]:
            n += 1
            result['APA_in_Sync'] = n
        elif apa[i]:
            o += 1
            result['APA_in_Async'] = o
        else:
            a += 1
            result['No_APA'] = a
    return result
