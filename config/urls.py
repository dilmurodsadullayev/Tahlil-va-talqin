from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from main.views import custom_404  # 404 sahifani render qilish uchun

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls"))
]

# # Faqat DEBUG=False bo‘lsa ham media fayllarni qo‘shish
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     from django.views.static import serve
#     from django.urls import re_path
#
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),]
#
# handler404 = custom_404


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
