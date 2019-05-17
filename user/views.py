from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm
from topo.models import Route, Crag, Sector, Region, Area
from .models import RouteRating






class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):

        if not request.user.is_anonymous:
            return HttpResponseRedirect('/')

        data = request.POST
        print(request.POST)
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/')

        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class RouteRateView(View):
    def post(self, request):
        type = request.POST['type']
        id = request.POST['id']

        current_user = request.user
        route = Route.objects.get(id=id)
        rating = request.POST['rate']


        RouteRating.objects.create(
            user=current_user,
            route=route,
            rating=rating,
        )
        return redirect(f'/{type}/{id}')

class SearchView(View):
    def get(self, request):

            area_name = request.GET['search']
            areas = Area.objects.filter(name__icontains=area_name)

            region_name = request.GET['search']
            regions = Region.objects.filter(name__icontains=region_name)

            sector_name = request.GET['search']
            sectors = Sector.objects.filter(name__icontains=sector_name)

            crag_name = request.GET['search']
            crags = Crag.objects.filter(name__icontains=crag_name)

            route_name = request.GET['search']
            routes = Route.objects.filter(name__icontains=route_name)

            ctx = {
                'areas': areas,
                'regions': regions,
                'sectors': sectors,
                'crags': crags,
                'routes': routes
            }

            return render(request, 'search.html', ctx)















