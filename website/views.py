from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "home.html", context)

