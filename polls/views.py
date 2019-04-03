from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from .models import Post
from django.utils import timezone
import datetime


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'polls/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'polls/post_list.html', {'posts' : posts})


#It's scheduled to ship on {{ date|date:"F j, Y" }}

#def index(request):
    #return render(request, 'polls/tem.html')


'''d = datetime.datetime.now()
t = Template("""<p>Dear {{ name }},</p>
<p> Thanks for placing an order from {{ company }}. It's shipped at {{ date }}.</p>
{% if warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% else %}
<p> You didn't order a warranty, so you're on your own when the products inevitably stop working.</p>
{% endif %}
<p>Sincerely,<br />{{ company }}</p>""")


c = Context({'name' : 'Tanmay', 'company' : 'Vanisb', 'date' : d, 'warranty' : True})
'''
