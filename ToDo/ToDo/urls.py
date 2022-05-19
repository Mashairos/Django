from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Rota Admin:
    path('admin/', admin.site.urls),
    # Demais Rotas:
    path('', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
