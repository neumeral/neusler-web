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
        context = {
            "seo_title": "Product and Features | Neusler",
            "seo_desc": "Neusler is a content publishing platform with a focus on reader experience and improving engagement. The main features being - publishing workflows for content teams, automations to keep your team productive, and interactive blocks to engage with your audience.",
        }
        return render(request, "product.html", context)


class ProductPubPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Publishing - Editing Interface and Workflows | Neusler",
            "seo_desc": "Leverage workflows, to streamline your editorial processes. Neusler features a clutter-free interface with configurable workflows. Built on wagtail — get the goodness of streamfield to manage mixed content types.",
            "seo_image": "images/neusler-ss_md.jpg"
        }
        return render(request, "product/publishing.html", context)


class ProductAutomatePageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Automations and integrations | Neusler",
            "seo_desc": "Using automations, you can integrate with connected Social Channels, push notifications and other systems using custom integrations.",
            "seo_image": "images/pages/integrations.jpg"
        }
        return render(request, "product/automate.html", context)


class ProductAIPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Content generation and analysis with AI | Neusler",
            "seo_desc": "Use the power of AI to create engaging content variations. With powerful personalizations and content recommendations, keep your readers captivated and keep coming for more.",
        }
        return render(request, "product/ai.html", context)


class ProductEngagePageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Interactive elements to increase user engagement | Neusler",
            "seo_desc": "Embed interactive blocks within your content, to give a unique experience to your readers, and improve retention. Create entertaining and valuable content to your readers - with web stories and bite sized content formats.",
            "seo_image": "images/pages/engage.jpg"
        }
        return render(request, "product/engage.html", context)


class PricingPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Plans and Pricing | Neusler",
            "seo_desc": "Find the plan that fits your needs - we offer great prices, premium products and quality service for your business.",
        }
        return render(request, "pricing.html", context)


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Contact us to know more | Neusler",
            "seo_desc": "Contact us to discuss how Neusler can improve content monetization and make your content marketing efficient.",
        }
        return render(request, "contact.html", context)


class CommunityPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "community.html", context)


class ToolsPageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "seo_title": "Open source content management tools  | Neusler",
            "seo_desc": "We believe in opensource. The core of neusler is opensource; and we use a lot of opensource tools and frameworks. This is how we give back to the community!",
            "seo_image": "images/oss.jpg"
        }
        return render(request, "tools.html", context)


class BlogListView(ListView):
    model = BlogPost
    paginate_by = 10
    ordering = ['-created']
