import datetime


def str_to_datetime(str) -> datetime.datetime:
    return datetime.datetime.strptime(str, "%Y-%m-%d")
