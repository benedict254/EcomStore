from django.urls import path
#from .views import  SearchResultsView
from .import views



urlpatterns = [
    #path('', views.item_list, name='item_list'),
    #path('<slug>', views.item_detail, name='item_detail'),
	path('',views.home,name='home'),
    #path('search/', SearchResultsView.as_view(), name='search_results'),
]



