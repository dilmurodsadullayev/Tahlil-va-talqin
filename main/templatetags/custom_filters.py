from django import template
from datetime import date
from datetime import datetime
import locale

register = template.Library()

@register.filter()
def article_date(value):
    if isinstance(value, datetime):
        locale.setlocale(locale.LC_TIME)
        return value.strftime("%d/%m/%Y")
    return value


uzbek_months = {
    "January": "Yanvar", "February": "Fevral", "March": "Mart",
    "April": "Aprel", "May": "May", "June": "Iyun",
    "July": "Iyul", "August": "Avgust", "September": "Sentabr",
    "October": "Oktabr", "November": "Noyabr", "December": "Dekabr"
}

@register.filter
def article_date_for(value):
    if isinstance(value, datetime):
        month = value.strftime("%B")  # Inglizcha oy nomi
        day = value.strftime("%d")    # Kun
        return f"{day} {uzbek_months.get(month, month)}"
    return value



