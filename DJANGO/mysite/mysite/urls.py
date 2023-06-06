from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('chapter/<id>/' , views.chapter),
    path('search/', views.search),
    path('blog/', include('blog.urls'))
]