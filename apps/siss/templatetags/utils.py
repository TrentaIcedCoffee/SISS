from django import template
from utils.messages import *

register = template.Library()

@register.filter
def get_attr(obj, name):
    return getattr(obj, name, '')
    
@register.filter
def success_msgs(msgs):
    return [msg for msg in msgs if msg.level == messages.SUCCESS]
    
@register.filter
def error_msgs(msgs):
    return [msg for msg in msgs if msg.level == messages.ERROR]
    