from .models import Category

def menu_links(request):
    links = Category.objects.all()
    links = sorted(links, key=lambda x: len(x.name))
    return {'links':links}