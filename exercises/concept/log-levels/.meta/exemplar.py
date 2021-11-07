from enum import Enum


class LogLevel(Enum):
    """Represent different log levels by their verbose codes."""

    TRACE = 'TRC'
    DEBUG = 'DBG'
    INFO = 'INF'
    WARNING = 'WRN'
    WARN = 'WRN'
    ERROR = 'ERR'
    FATAL = 'FTL'
    UNKNOWN = 'UKN'


class LogLevelInt(Enum):
    """Represents different logging levels by their short codes"""

    TRACE = 0
    DEBUG = 1
    INFO = 4
    WARNING = 5
    WARN = 5
    ERROR = 6
    FATAL = 7
    UNKNOWN = 42


def parse_log_level(message):
    """Takes a log message and returns the enum member of its level
    Returns a LogLevel.Unknown incase an unknown severity is found

    :param message: log message (string)
    :return: <enum 'LogLevel'>

    Ex:
    - parse_log_level("[INF]: File deleted") #=> LogLevel.Info
    - parse_log_level("[XYZ]: Out of context message") #=> LogLevel.Unknown
    """

    str_split = message.split(':')
    lvl = str_split[0][1:-1]
    if lvl in [level.value for level in LogLevel]:
        return LogLevel(lvl)
    return LogLevel('UKN')


def convert_to_short_log(log_level, message):
    """Converts a log message to a shorter format optimized for storage.

    :param log_level: The Log level of the log sent. ex: LogLevel.Error.
    :param message: log message (string)
    :return: <enum 'LogLevelInt'>

    Ex:
    - convert_to_short_log(LogLevel.Error, "Stack overflow") #=> "6:Stack overflow"
    """

    return f'{LogLevelInt[log_level.name].value}:{message}'


def get_warn_alias():
    """Returns the enum for LogLevel Warning

    :return: <enum 'LogLevel'>
    """

    return LogLevel('WRN')


def get_members():
    """Returns a list of tuples (name, value) containing all the members
    of the enum LogLevel.

    :return: List of tuples [(name1, value1), (name2, value2)]
    """

    out_list = []
    for member in LogLevel:
        out_list.append((member.name, member.value))
    return out_list
