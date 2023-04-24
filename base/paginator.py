from django.core.paginator import Paginator
from . views import all_houses


page = 1
results = 10
paginator = Paginator(all_houses, results)
# paginator2 = Paginator(, results)

houses = paginator.page(page)