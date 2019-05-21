from django.shortcuts import render, redirect
from django.views import View
from topo.models import Route, Crag, Sector, Region, Area
from .models import RouteRating
from django.contrib import messages
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'user_registration.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Stworzono użytkownika {username}! Możesz się zalogować!')
            return redirect('/login')
        else:
            form = UserRegisterForm(request.POST)
            return render(request, 'user_registration.html', {'form': form})

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

    def post(self, request):

            area_name = request.POST['search']
            areas = Area.objects.filter(name__icontains=area_name)

            region_name = request.POST['search']
            regions = Region.objects.filter(name__icontains=region_name)

            sector_name = request.POST['search']
            sectors = Sector.objects.filter(name__icontains=sector_name)

            crag_name = request.POST['search']
            crags = Crag.objects.filter(name__icontains=crag_name)

            route_name = request.POST['search']
            routes = Route.objects.filter(name__icontains=route_name)

            ctx = {
                'areas': areas,
                'regions': regions,
                'sectors': sectors,
                'crags': crags,
                'routes': routes
            }

            return render(request, 'search.html', ctx)















