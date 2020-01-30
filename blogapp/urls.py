"""kivabejabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact, name="contact"),
    path('submission', views.submission, name="submission"),
    path('article/<int:id>', views.blogger, name="blog2"),
    path('content/<int:id>', views.content, name="blog3"),
    path('livingcost/<int:id>', views.livingcost, name="blog4"),
    path('earning/<int:id>', views.earning, name="blog5"),
    path('embassy_address/<int:id>', views.embassy_address, name="blog6"),
    path('ticket_price/<int:id>', views.ticket_price, name="blog7"),
    path('count', views.count,name="count"),
    path('counts', views.counts,name="counts"),
    path('search', views.search, name="search"),

]
