from datetime import datetime

from django.conf import settings


def default(request):
    return {
            "default_title": "Modern Content Publishing Platform | Neusler",
            "default_desc": "Neusler is a content publishing platform with workflows, automations, interactive elements, monetization modules and much more. Focus on creating great content, while Neulser handles reader experience and distribution.",
            "server_time": datetime.now(),
            "ga4_id": settings.GOOGLE_ANALYTICS4_ID or None
        }
