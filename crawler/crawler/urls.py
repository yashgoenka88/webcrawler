
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CrawlerView


urlpatterns = [
    url(r'^crawl/$', CrawlerView.as_view(), name='crawler_viewset'),
    url('^.*$',TemplateView.as_view(template_name="index.html")),

]
