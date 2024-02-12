from django.contrib.auth.views import LogoutView
from django.urls import path, include
from apps.views import IndexView, ProductsListView, AddProductView, DeleteProductView, RegisterFormView, CustomLoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('product-list', ProductsListView.as_view(), name='product_list_page'),
    path('add_product', AddProductView.as_view(), name='add_product_page'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete_product_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('logout', LogoutView.as_view(next_page='login_page'), name='logout_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
