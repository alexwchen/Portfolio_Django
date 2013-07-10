from django import template 
register = template.Library()

@register.filter
def split_detail(value):

    oldlist = value.split(' ')
    newlist = []
    for i in oldlist:
        if len(i)!=0:
            newlist.append(i)
    return newlist


