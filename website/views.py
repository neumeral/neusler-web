from django.shortcuts import render
from django.views.generic import ListView, View

from website.models import BlogPost


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        request.session['record'] = True
        return render(request, "home.html", context)


class ProductPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "product.html", context)


class ProductPubPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "product/publishing.html", context)


class ProductAutomatePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "product/automate.html", context)


class ProductAIPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "product/ai.html", context)


class ProductEngagePageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "product/engage.html", context)


class PricingPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "pricing.html", context)


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)


class CommunityPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "community.html", context)


class ToolsPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "tools.html", context)


class BlogListView(ListView):
    model = BlogPost
    paginate_by = 10
    ordering = ['-created']
