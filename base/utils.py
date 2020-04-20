import datetime


def time2str(d):
    if d:
        str = datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')
    else:
        str = ''
    return str


def str2time(s):
    try:
        d = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    except Exception, e:
        d = None
    finally:
        return d