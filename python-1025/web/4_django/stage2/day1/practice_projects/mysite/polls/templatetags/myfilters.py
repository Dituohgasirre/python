from django import template

register = template.Library()

@register.filter(name="mine")
def do_mine(val):
    return 'modified by customized filter: %s' % val


@register.simple_tag
def errmsg(errlist):
    if errlist:
        return errlist[0]
    else:
        return ''
