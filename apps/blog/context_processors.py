from .models import Post
from .models import BlogGroup

def global_data(request):
    post = Post.objects.order_by('-publish_date')[:5]
    blog_group = BlogGroup.objects.order_by('members')[:5]
    data = { 'top_post': post, 'top_groups': blog_group }
    return data