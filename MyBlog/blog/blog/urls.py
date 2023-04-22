"""iblogs URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# for changing authontication 
admin.site.site_header = 'My Blog'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"

# for hosting below two lines added
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog2nd.urls')),
                #  for hosting below two lines added
                  url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
                  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    