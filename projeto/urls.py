from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# Http request


def my_view(request):
    return HttpResponse('Una linda string')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view)
]
