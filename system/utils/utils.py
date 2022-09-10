

def format_date(date_str: str) -> str:
    """
    Standardizes date strings in the format year-month-day (eg: 2022-01-04).

    Args:
        date_str: The string containing containing a date.
    Returns:
        A string containing the date formated.
    """

    # check if the date is in the 'week day, month day, year' format (eg: Thu, 06 Jan 2022)
    if date_str[:3].isalpha():
        months_to_numbs = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07',
                           'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        date_str = date_str[5:16]
        day, month, year = date_str.split(' ')
        month = months_to_numbs[month]
        return year + '-' + month + '-' + day
    return date_str[:10]


def sort_dict_list_by_date(items: list):
    """Sort the list elements by date order"""

    items.sort(key=lambda x: x['date'])
