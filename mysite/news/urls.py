from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from news.models import Articles
from django.conf.urls import url

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    re_path(r'^(?P<pk>\d+)', DetailView.as_view(model=Articles, template_name="news/post.html"))
]


