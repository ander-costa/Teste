from django.conf.urls import include, url
import AnderApp.views

# Django processes URL patterns in the order they appear in the array

urlpatterns = [
    url(r'^$', AnderApp.views.index, name='index'),
    url(r'^home$', AnderApp.views.index, name='home'),
]