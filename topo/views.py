from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Area, Region, Sector, Crag, Route
from user.models import RouteRating, CragRating, SectorRating, RegionRating, AreaRating
from django.db.models import Avg


# Create your views here.

class IndexView(View):
    def get(self, request):
        area = Area.objects.all()
        return render(request, 'index.html', {'area': area})

class AreaListView(View):
    def get(self, request):
        area = Area.objects.all()
        return render(request, 'area_list.html', {'area': area})

class AreaView(View):
    def get(self, request, area_id):
        area = Area.objects.get(id=area_id)
        area_regions = area.region_set.all
        rating = AreaRating.objects.aggregate(Avg('rating'))['rating__avg']
        if rating is not None:
            avg_rating = round(rating, 1)
        else:
            avg_rating = 0

        return render(request, 'area.html', {'area': area, 'area_regions': area_regions, 'avg_rating': avg_rating})

class AreaRegionView(View):
    def get(self, request, region_id):
        region = Region.objects.get(id=region_id)
        region_sectors = region.sector_set.all()
        rating = RegionRating.objects.aggregate(Avg('rating'))['rating__avg']
        if rating is not None:
            avg_rating = round(rating, 1)
        else:
            avg_rating = 0

        return render(request, 'region.html', {'region': region, 'region_sectors': region_sectors, 'avg_rating': avg_rating})

class RegionSectorView(View):
    def get(self, request, sector_id):
        sector = Sector.objects.get(id=sector_id)
        sector_crags = sector.crag_set.all()
        rating = SectorRating.objects.aggregate(Avg('rating'))['rating__avg']
        if rating is not None:
            avg_rating = round(rating, 1)
        else:
            avg_rating = 0

        return render(request, 'sector.html', {'sector': sector, 'sector_crags': sector_crags, 'avg_rating': avg_rating})

class SectorCragView(View):
    def get(self, request, crag_id):
        crag = Crag.objects.get(id=crag_id)
        crag_routes = crag.route_set.all()
        rating = CragRating.objects.aggregate(Avg('rating'))['rating__avg']
        if rating is not None:
            avg_rating = round(rating, 1)
        else:
            avg_rating = 0

        return render(request, 'crag.html', {'crag': crag, 'crag_routes': crag_routes, 'avg_rating': avg_rating})

class RouteView(View):
    def get(self, request, route_id):
        route = Route.objects.get(id=route_id)
        rating = RouteRating.objects.filter(route_id=route_id).aggregate(Avg('rating'))['rating__avg']
        if rating is not None:
            avg_rating = round(rating, 1)
        else:
            avg_rating = 0

        return render(request, 'route.html', {'route': route, 'type': 'route', 'id': route.id, 'avg_rating': avg_rating})

















