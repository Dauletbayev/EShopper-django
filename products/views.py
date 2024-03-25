from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from products.handler import bot
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from products.models import CategoryModel, ProductModel, CartModel
from products.forms import SearchForm


class HomePage(ListView):
    form = SearchForm
    template_name = 'index.html'
    model = ProductModel
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["products"] = ProductModel.objects.all()
        return context

def main_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='index.html', context=context)

def shop_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='shop.html', context=context)

def detail_page(request, pk):
    categories = CategoryModel.objects.all()
    product = ProductModel.objects.get(id=pk)
    context = {'product': product, 'categories': categories}
    return render(request, template_name='detail.html', context=context)

def cart_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='cart.html', context=context)

def checkout_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='checkout.html', context=context)

def contact_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='contact.html', context=context)

def category_page(request, pk):
    categories = CategoryModel.objects.all()
    category = CategoryModel.objects.get(id=pk)
    current_products = ProductModel.objects.filter(product_category=category)
    context = {'product': current_products, 'categories': categories}
    return render(request, template_name='category.html', context=context)

class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

def logout_view(request):
    logout(request)
    return redirect('home')

def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(product_title__icontains=get_product)
            return redirect(f'/detail/{exact_product.id}')
        except:
            return redirect('/')

def sort_view(request):
    data = ProductModel.objects.all()

    sort_by = request.GET.get('sort_by')
    if sort_by:
        if sort_by == 'Latest':
            data = data.order_by('-product_created_at')
        elif sort_by == 'Earliest':
            data = data.order_by('product_created_at')

    return render(request, 'shop.html', {'data': data})


def add_products_to_user_cart(request, pk):
    if request.method == 'POST':
        checker = ProductModel.objects.get(pk=pk)

        if checker.product_count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id,
                                     user_product=checker,
                                     user_product_count=int(request.POST.get('pr_count'))
                                     ).save()
            print('Success')
            return redirect('cart')
        else:
            return redirect('/')

def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Новый заказ\n'
        for i in cart:
            main_text += (f'Товар: {i.user_product}\n'
                          f'Количество: {i.user_product_count}\n'
                          f'Покупатель: {i.user_id}\n'
                          f'Цена товара: {i.user_product.product_price}\n')
            bot.send_message(-1001835453645, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, template_name='cart.html', context={'cart': cart})

def delete_user_cart(request, pk):
    product_delete = ProductModel.objects.get(pk=pk)

    CartModel.objects.filter(user_id=request.user.id,
                             user_product=product_delete).delete()
    return redirect('/user_cart')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Registration')
        context.update(user_context)
        return context

    def get_user_context(self, **kwargs):
        return {
            'title': kwargs.get('title', 'Registration')
        }
