from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.images,name = 'image'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),
    url(r'^comment/(\d+)', views.comment, name='comment'),
    url(r'rate/(\d+)', views.rate, name='rate'),
    url(r'^search/', views.search_picture, name='search_picture'),
    url(r'^api/merch/$', views.MerchSerializer.as_view(),name="jacky"),
    url(r'^api/pro/$', views.ProSerializer.as_view(),name="mukamisha"),
    
    
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
  