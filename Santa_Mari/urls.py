from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Santa_Mari import views

urlpatterns = [
                  path('', views.ProductListView.as_view(), name='list-product'),
                  # path('detail-product/<slug:slug>', views.ProductDetailView, name='detail-product')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
