from django_distill import distill_path

from .views import (ContactPageView, HomePageView, PricingPageView,
                    ProductAutomatePageView, ProductEngagePageView,
                    ProductPageView, ProductPubPageView, ToolsPageView)


def get_static_template():
    return None


urlpatterns = [
    distill_path(
        "",
        HomePageView.as_view(),
        name="home_page",
        distill_func=get_static_template,
        distill_file="index.html",
    ),

    distill_path(
        "product/",
        ProductPageView.as_view(),
        name="product_page",
        distill_func=get_static_template,
        distill_file="product/index.html",
    ),

    distill_path(
        "product/publishing/",
        ProductPubPageView.as_view(),
        name="product_publishing_page",
        distill_func=get_static_template,
        distill_file="product/publishing/index.html",
    ),

    distill_path(
        "product/automate/",
        ProductAutomatePageView.as_view(),
        name="product_automate_page",
        distill_func=get_static_template,
        distill_file="product/automate/index.html",
    ),

    # distill_path(
    #     "product/ai",
    #     ProductAIPageView.as_view(),
    #     name="product_ai_page",
    #     distill_func=get_static_template,
    #     distill_file="product/ai/index.html",
    # ),

    distill_path(
        "product/engage/",
        ProductEngagePageView.as_view(),
        name="product_engage_page",
        distill_func=get_static_template,
        distill_file="product/engage/index.html",
    ),

    distill_path(
        "drops/",
        ToolsPageView.as_view(),
        name="drops_page",
        distill_func=get_static_template,
        distill_file="drops/index.html",
    ),

    distill_path(
        "pricing/",
        PricingPageView.as_view(),
        name="pricing_page",
        distill_func=get_static_template,
        distill_file="pricing/index.html",
    ),

    distill_path(
        "contact/",
        ContactPageView.as_view(),
        name="contact_page",
        distill_func=get_static_template,
        distill_file="contact/index.html",
    ),

]
