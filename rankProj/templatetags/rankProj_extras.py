from django import template 

# this is where all tags and filter are registered
register = template.Library()

@register.filter
def split_img(value):

    oldlist = value.split(' ')
    newlist = []
    for i in oldlist:
        if len(i)!=0:
            newlist.append(i)
    return newlist


@register.filter
def split_content(value):

    value = value.replace("\r","@")
    value = value.replace("\t","@")
    oldlist = value.split('\n')

    newlist = []
    for i in oldlist:
        if i!='@' and i!='':
            newlist.append(i.replace('@', ''))
    return newlist


@register.filter
def pathfilt(value):

    value = value.split("/")[1]
    return value


@register.filter
def split_detail(value):

    oldlist = value.split(' ')
    newlist = []
    for i in oldlist:
        if len(i)!=0:
            newlist.append(i[:-1])
    return newlist


@register.simple_tag
def access_lock(value, arg):

    if value[arg] == 0:
        return 'none'
    else:
        return 'block'
