from django.conf.urls.static import static
from django.urls import path

from apps.views import ProductListView, delete_product, update_product
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('', ProductListView.as_view(), name='index'),
                  path('delete-product/<int:pk>', delete_product, name='delete_todo'),
                  path('update-product/<int:pk>', update_product, name='update_todo'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
