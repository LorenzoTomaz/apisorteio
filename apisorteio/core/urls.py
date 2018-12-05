from django.urls import path, include
from apisorteio.core.views import ApiSorteio

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('sorteio/', ApiSorteio.as_view({"get": "sorteio_api"})),
    path('sorteio_loja/', ApiSorteio.as_view({"get": "sorteio_api_loja"}))
]
