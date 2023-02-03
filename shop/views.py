from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Product
from .forms import EmailPostForm


def index(request):
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{}'.format(cd['email'])
            message = 'Read at \n\n{}\'s comments: {}'.format( cd['email'], cd['email'])
            # send_mail(subject, message, 'yulia.antonova225@gmail.com', [cd['to']])
            send_mail(subject, message, 'yulia.antonova225@gmail.com', [cd['email']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'web/index.html', {'form': form, 'sent': sent})


def shop(request):
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'web/shop.html', {'page': page,
    'products': products})


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'web/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'web/detail.html')


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}'.format(post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            # send_mail(subject, message, 'yulia.antonova225@gmail.com', [cd['to']])
            send_mail(subject, message, 'yulia.antonova225@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'web/post_share.html', {'post': post, 'form': form, 'sent': sent})


def product(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product
    }
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session["session_key"]=123
    #     request.session.cycle_key()
    #     print(request.session.session_key)
    return render(request, 'web/product.html', context)


def password_reset_request(request):
    context = {

    }
    return render(request, 'registration/password_reset_form.html', context)



