"""
messcover URL Configuration
"""
from django.conf.urls import url
from messcover.views import IndexView, TreeView, CrawlView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^start/$', CrawlView.as_view(), name='start_crawl'),
    url(r'^tree/', TreeView.as_view(), name='tree'),
]
