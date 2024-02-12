from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('-id')


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect('index')


def update_product(request, pk):
    if request.method == 'POST':
        Product.objects.filter(id=pk).update(title=request.POST['title'], content=request.POST['content'])
        return redirect('index')
    context = {
        'product': Product.objects.filter(id=pk)
    }
    return render(request, 'update_product.html', context)
