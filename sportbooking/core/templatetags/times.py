# core/templatetags/times.py

from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def times_until(start_hour, end_hour):
    """
    Generuje časy od start_hour do end_hour ve formátu HH:MM.
    """
    start_time = datetime.strptime(str(start_hour), "%H")
    end_time = datetime.strptime(str(end_hour), "%H")
    time_list = []

    while start_time < end_time:
        time_list.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=30)
    
    return time_list
