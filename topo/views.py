from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Area, Region, Sector, Crag, Route


# Create your views here.

class IndexView(View):
    def get(self, request):
        areas = Area.objects.all()
        return render(request, 'index.html', {'areas': areas})

class AreaView(View):
    def get(self, request):
        areas = Area.objects.all()
        return render(request, 'area.html', {'areas': areas})

class AreaRegionView(View):
    def get(self, request, area_id):
        area = Area.objects.get(id=area_id)
        area_regions = area.region_set.all()
        return render(request, 'area_regions.html', {'area': area, 'area_regions': area_regions})

class RegionSectorView(View):
    def get(self, request, region_id):
        region = Region.objects.get(id=region_id)
        region_sectors = region.sector_set.all()
        return render(request, 'region_sectors.html', {'region': region, 'region_sectors': region_sectors})

class SectorCragView(View):
    def get(self, request, sector_id):
        sector = Sector.objects.get(id=sector_id)
        sector_crags = sector.crag_set.all()
        return render(request, 'sector_crags.html', {'sector': sector, 'sector_crags': sector_crags})

class CragRouteView(View):
    def get(self, request, crag_id):
        crag = Crag.objects.get(id=crag_id)
        crag_routes = crag.route_set.all()
        return render(request, 'crag_routes.html', {'crag': crag, 'crag_routes': crag_routes})

class RouteView(View):
    def get(self, request, route_id):
        route = Route.objects.get(id=route_id)
        return render(request, 'route.html', {'route': route, 'type': 'route', 'id': route.id})

















