from django import template

register = template.Library()


@register.filter
def to_stars(value):
    try:
        count = int(value)
    except Exception:
        return "Can't use a filter"
    if count == 0:
        return "No stars"

    return "🌟" * count


@register.filter
def bestseller_label(value):
    try:
        boolean = bool(value)
    except Exception:
        return "Can't use a filter"
    if boolean:
        return "Bestseller"+"✅"
    return ""
@register.simple_tag
def popular(value):
    try:
        count = int(value)
    except Exception:
        return "Can't use a filter"
    if count >=4:
        return "This is popular book, try it"
    return "This is book is not popular, maybe hidden gem?"
