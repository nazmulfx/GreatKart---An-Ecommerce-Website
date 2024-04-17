
from . models import Category

## Note: It's a function, It takes request as an arguments and return dictionary of data as a context
def menu_links(request):
    
    # patch all the category data from the database and return as Dictionary
    # like this: {'links': <QuerySet [<Category: Shirts>, <Category: T Shirts>, <Category: shoes>, <Category: Jeans>, <Category: Jacket>]>}
    links = Category.objects.all()

    return dict(links=links)