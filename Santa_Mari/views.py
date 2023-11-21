from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Category, Product


class ProductListView(ListView):
    template_name = 'Santa_Mari/Product/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_product = self.request.GET.get('search_product') or ''
        if search_product:
            context['products'] = context['products'].filter(name__startswith=search_product)

        context['search_product'] = search_product  # The entered word remains in the search box
        return context


class ProductDetailView(DetailView):
    template_name = 'Santa_Mari/Product/product_detail.html'
    model = Product
    context_object_name = 'product'
