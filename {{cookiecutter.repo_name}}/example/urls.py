from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('{{ cookiecutter.app_name }}.urls', namespace='{{ cookiecutter.app_name }}')),
]
