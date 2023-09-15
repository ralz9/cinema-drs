
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="cinematica",
      default_version='v1',
      description="online cinema",
      contact=openapi.Contact(email="RodionDereha@gmail.com"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/account/', include('applications.account.urls')),
    path('api/movie/', include('applications.cinema.urls'))
]
