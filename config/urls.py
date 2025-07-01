from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cats/', include('cats.urls')),
    # path('api/', include('adoptions.urls')),  # 라희님
    # path('api/', include('users.urls')),     # 우진님
]
