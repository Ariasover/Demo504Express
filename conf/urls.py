"""504Express URLs."""
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('configuration/', TemplateView.as_view(template_name="configuration.html",)),

    path('configuration/',TemplateView.as_view(template_name='configuration.html'),name='configuration'),

    path('', include(('apps.users.urls', 'users'), namespace='users')),
    path('', include(('apps.messagesconf.urls', 'messagesconf'), namespace='messagesconf')),
    path('', include(('apps.speech.urls', 'speech'), namespace='speech')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
