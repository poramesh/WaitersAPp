from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Order
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'orders' : Order.objects.all()
    }
    return render(request,'orders/order.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'orders'
    ordering = ['dateTimeOrdered']



class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['staff','drinks','starter','main','desserts','TableInfo','CustName','RestName','bill']

    def form_valid(self,form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['staff','drinks','starter','main','desserts','TableInfo','CustName','RestName','bill']

    def form_valid(self,form):
        form.instance.staff = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.staff:
            return True
        return False
    
class OrderDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Order
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.staff:
            return True
        return False

    
def about(request):
    return render(request,'orders/about.html',{'title': 'orders'})

