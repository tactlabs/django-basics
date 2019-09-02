from django.shortcuts import render

posts = [
    {
        'author' : 'Raja',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'Sep 02, 2019'
    },

    {
        'author' : 'Mike',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'Sep 01, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts,
        'title' : 'Home Page'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About Page'})