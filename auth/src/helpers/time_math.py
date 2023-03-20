from datetime import datetime
from math import ceil

def dif_time(exp):
    now = datetime.now().timestamp()
    return ceil(exp - now)