from django.urls import path
from . import views

urlpatterns = [

    path('contact/',views.contact,name='contact'),
    path('products/',views.products,name='products'),
    path('news/',views.PostIndex.as_view(),name='news'),
    path('team/',views.team,name='team'),
    path('blog/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('',views.home,name='home'),
]
