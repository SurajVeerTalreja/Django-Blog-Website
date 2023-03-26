<<<<<<< HEAD
from django.shortcuts import render
from datetime import date

# Create your views here.
all_blog_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "SVTian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "SVTian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "SVTian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def home_page(request):
    sorted_posts = sorted(all_blog_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    context = {
        'posts': latest_posts,
    }
    return render(request, 'blog/home.html', context=context)

def all_posts(request):
    context = {
        'posts': all_blog_posts,
    }
    return render(request, 'blog/posts.html', context=context)


def blog_post(request, slug):
    # Match the post with the provided slug
    # We will use next() built in function to search through all the slugs using list comprehension
    identified_post = next(post for post in all_blog_posts if post['slug'] == slug)

    context = {
        'post': identified_post,
    }

    return render(request, 'blog/blog_post.html', context=context)
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Post
from django.views.generic import TemplateView, ListView, CreateView, View
from .forms import CommentForm


# Create your views here.
class PostTempelateView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_posts = Post.objects.all().order_by('-date')[:3]
        context["latest_posts"] = latest_posts 
        return context
    

class PostListView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    queryset = Post.objects.all().order_by('-date')
    context_object_name = 'posts'


class PostDetailView(View):
    # Defined method to reduce code and repeatation
    def is_read_later_post(self, request, post_id):
        read_later_posts_ids = request.session.get('read_later_posts')
        if read_later_posts_ids is not None:
            read_later_pressed = post_id in read_later_posts_ids
        else:
            read_later_pressed = False
        
        return read_later_pressed

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tags.all()
        form = CommentForm()
        post_comments = post.comments.all()

        context = {
            'post': post,
            'tags': tags,
            'form': form,
            'comments': post_comments,
            'read_later_pressed': self.is_read_later_post(request, post.id)
        }
        return render(request, 'blog/blog_post.html', context=context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('post-page', args=[slug]))
        
        # if form is not valid, render the pre-filled form with error messages
        tags = post.tags.all()
        post_comments = post.comments.all()
        context = {
            'post': post,
            'tags': tags,
            'form': form,
            'comments': post_comments,
            'read_later_pressed': self.is_read_later_post(request, post.id)
        }
        return render(request, 'blog/blog_post.html', context=context)

class ReadLaterView(View):
    def get(self, request):
        read_later_posts_ids = request.session.get('read_later_posts')
        
        context = {}
        # If no post is stored in Read Later
        if read_later_posts_ids is None or len(read_later_posts_ids) == 0:
            context['read_later_posts'] = []
            context['list_is_empty'] = True
        else:
            # If list is not Empty
            # Filter the list that are added to Read Later Session List
            all_read_later_posts = Post.objects.filter(pk__in=read_later_posts_ids)
            context['read_later_posts'] = all_read_later_posts
            context['list_is_empty'] = False
            
        return render(request, 'blog/read-later-posts.html', context=context)
    
    def post(self, request):
        read_later_posts_ids = request.session.get('read_later_posts')

        if read_later_posts_ids is None or len(read_later_posts_ids) == 0:
            read_later_posts_ids = []

        # Collect post id from submitted form
        # If post id is not in list id, add it, otherwise delete it.
        # If it is not added, post detail view will show 'Read Later' button
        # Otherwise it will show 'Delete from Read Later' button
        # Check blog_post html
        post_id = int(request.POST.get('post_id'))
        if post_id not in read_later_posts_ids: 
            read_later_posts_ids.append(post_id)
        else:
            read_later_posts_ids.remove(post_id)
            # request.session['read_later_posts_ids'] += [(request.POST['post_id'])]
        request.session['read_later_posts'] = read_later_posts_ids
        
        return redirect(reverse('home-page'))


# Function Based Views
# def home_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]

#     context = {
#         'latest_posts': latest_posts
#     }
#     return render(request, 'blog/index.html', context=context)


# def all_posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         'posts': all_posts
#     })


# def post(request, slug):
#     blog_post = get_object_or_404(Post, slug=slug)
#     all_tags = blog_post.tags.all()
#     return render(request, 'blog/blog_post.html', {
#         'post': blog_post,
#         'tags': all_tags,
#     } )
>>>>>>> 0eb7a81 (Blog Website Up and Running)
