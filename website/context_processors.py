from datetime import datetime


def default(request):
    return {
            "default_title": "Modern Content Publishing Platform | Neusler",
            "default_desc": "Neusler is a content publishing platform with workflows, automations, interactive elements, monetization modules and much more. Focus on creating great content, while Neulser handles reader experience and distribution.",
            "server_time": datetime.now()
        }
