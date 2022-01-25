from django.urls import path
from .api import CartCreateApi
from .api import CartListApi
from .api import CartDestroyApi
from .api import CartUpdateApi


urlpatterns = [
    path('api/create',CartCreateApi.as_view()),
    path('api/',CartListApi.as_view()),
    path('api/destroy/<int:pk>',CartDestroyApi.as_view()),
    path('api/update/<int:pk>',CartUpdateApi.as_view()),
]