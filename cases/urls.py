from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^cases/', TemplateView.as_view(template_name='cases/list.html')),
]
