from django.shortcuts import render,get_object_or_404
from .models import *
#from django.views.generic import TemplateView, ListView
#from django.db.models import Q

"""class SearchResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        return object_list
"""

def home(request):
	slides = slider.objects.all().order_by('id')[:7]
	context = {'slides':slides}
	return render(request,'home.html',context)

"""def item_list(request):
    item = Item.objects.all()

    return render(request, 'index.html', {'item': item})

def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)

    return render(request, 'item_detail.html', {'item': item})
"""


