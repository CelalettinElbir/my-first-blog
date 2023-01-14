from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CategoryCreateModel
# Create your views here.


# def home(request):

#     context = {

#         'posts': Post.objects.all(),
#         'title': 'deneme',

#     }

#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content']
    form_class = CategoryCreateModel

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()  

        for category in form.cleaned_data['categories']:
            selected_category = Category.objects.get(name=category)
            print(selected_category,self.object)
            selected_category.posts.add(self.object)


        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'blog/category.html'
#     context_object_name = 'categories'
#     paginate_by = 6


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category-posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.all()
        categories = Category.objects.all()
        context['categories'] = categories
        context['posts'] = posts
        return context


def about(request):
    return render(request, 'blog/about.html', {'title': 'naber'})
