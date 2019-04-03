from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
import datetime


#def index(request):
    #return render(request, 'polls/tem.html')

def post_list(request):
    return render(request, 'polls/post_list.html', {})


#It's scheduled to ship on {{ date|date:"F j, Y" }}
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
