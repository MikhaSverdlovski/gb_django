from django.shortcuts import render
from django.views.generic import TemplateView
import logging

# Создаем логгер для views
logger = logging.getLogger('landing.views')  # Рекомендуется использовать иерархические имена


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # Логируем информацию о запросе
        logger.info(
            f"HomePageView accessed by {request.user}",
            extra={'user': request.user.username}
        )
        return super().get(request, *args, **kwargs)



class InfoPageView(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        # Логируем информацию о запросе
        logger.info(
            f"InfoPageView accessed by {request.user}",
            extra={'user': request.user.username}
        )
        return super().get(request, *args, **kwargs)
