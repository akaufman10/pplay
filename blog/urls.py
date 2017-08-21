from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
        url(r'^login/$', auth_views.login, {'template_name':'blog/login.html'},name='login'),
        url(r'^logout/$', auth_views.logout, {'next_page': '/home'}, name='logout'),
        url(r'^admin/', admin.site.urls),
	url(r'^$', views.loading, name='loading'),
	url(r'^about', views.about, name='about'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^thanks', views.thanks, name='thanks'),
	url(r'^home$', views.home, name='home'),
	url(r'^play/(?P<pk>\d+)/$', views.play_detail, name='play_detail'),
	url(r'^play/(?P<pk>\d+)/edit/$', views.play_edit, name='play_edit'),
	url(r'^play/new/$', views.play_new, name='play_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

        
