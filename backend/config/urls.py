from django.contrib import admin
from django.urls import path
from apps.users.api import router as auth_router
from ninja import NinjaAPI
from django.views.generic import TemplateView

api = NinjaAPI(title="Logbook360 API", version="1.0", docs_url="/docs")

api.add_router('/auth', auth_router)

urlpatterns = [
    path("custom_admin/", admin.site.urls),
    path("api/", api.urls),
    path('swagger/', TemplateView.as_view(template_name="swagger-ui/index.html")),
]
