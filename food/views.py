from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import Post, Comment, Category
from django.utils.decorators import method_decorator
from functools import wraps
from django.core.exceptions import PermissionDenied
from .forms import CommentForm, PostForm


def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))


# for post view
class PostList(generic.ListView):

    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.

    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`food/index.html`
    """

    queryset = Post.objects.filter(status=1)
    template_name = "food/index.html"
    paginate_by = 6


def post_detail(request, slug):

    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
    An instance of :model:`blog.Post`.

    **Template:**

    :template:`food/food.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()

    return render(
        request,
        "food/food.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(
        request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    cats_lower = cats.lower()
    try:
        category = Category.objects.get(name__iexact=cats_lower)
        category_posts = Post.objects.filter(category=category)
    except Category.DoesNotExist:
        category_posts = Post.objects.none()

    cat_menu = Category.objects.all()

    return render(request, 'categories.html', {
        'cats': cats.title(
        ), 'category_posts': category_posts, 'cat_menu': cat_menu})


# for editting comment
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# for deleting comment
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# for adding categories
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
