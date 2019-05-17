"""myTopo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from topo.views import AreaListView, AreaView, AreaRegionView, RegionSectorView, SectorCragView, RouteView, IndexView
from user.views import LoginView, LogoutView, RouteRateView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', IndexView.as_view()),
    re_path(r'^area_list$', AreaListView.as_view()),
    re_path('^area/(?P<area_id>(\d)+)$', AreaView.as_view()),
    re_path('^region/(?P<region_id>(\d)+)$', AreaRegionView.as_view()),
    re_path('^sector/(?P<sector_id>(\d)+)$', RegionSectorView.as_view()),
    re_path('^crag/(?P<crag_id>(\d)+)$', SectorCragView.as_view()),
    re_path('^route/(?P<route_id>(\d)+)$', RouteView.as_view()),
    re_path('^login$', LoginView.as_view()),
    re_path('^logout$', LogoutView.as_view()),
    re_path(r'^rate$', RouteRateView.as_view()),
    re_path(r'^search$', SearchView.as_view()),
]
