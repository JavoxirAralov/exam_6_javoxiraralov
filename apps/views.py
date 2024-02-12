from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic.edit import DeleteView

from apps.forms import ProductForm, RegisterForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import Product


class IndexView(TemplateView):
    template_name = 'apps/home.html'


class RegisterFormView(FormView):
    template_name = 'apps/profile/login.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'apps/profile/login.html'
    next_page = 'index_page'


class ProductsListView(ListView):
    template_name = 'apps/product/product-list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class AddProductView(CreateView):
    template_name = 'apps/product/products_with_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list_page')


class DeleteProductView(DeleteView):
    template_name = 'apps/product/product-list.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_list_page')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super().form_valid(form)
