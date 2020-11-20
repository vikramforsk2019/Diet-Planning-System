from django.urls import path,re_path
from . import views
from django.conf.urls import url
app_name = 'dietapp'

urlpatterns = [
    path('', views.index, name='homepage'),
path('health_post/', views.health_post, name='health_post'),
path('health_data/', views.health_data, name='health_data'),
path('alltype/', views.alltype, name='alltype'),
 re_path(r'^category/(?P<username>[.@_+\w-]+)$', views.category, name='cat'),
url(r'single/(?P<postid>\d+)/$', views.single, name='single'),
#path(r'single/(?P<postid>\d+)/$', views.single, name='single'),
]


"""

How To Pass Parameters To View Via Url In Django
<td><a href="{% url 'dept_emp:emp_detail' user_name=emp.user.username mobile_number=emp.emp_mobile %}">{{ emp.user.username }}</a></td>

url(r'^emp_detail/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', views.emp_detail, name='emp_detail'),

The (?P<user_name>\w+) section means this is a url parameter (?P), 
and the parameter value should be passed to views.emp_detail function’s user_name argument. 
The \w+ is a regular expression which means this url parameter’s value should be more than 
one charactor or digits.

@login_required()
def emp_detail(request, user_name, mobile_number):

"""