from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
''' Мы связали view под именем post_list с 
URL-адресом ^$. Это регулярное выражение 
будет соответствовать ^ (началу) и следующему $
(концу), т.е. пустой строке.
Этот шаблон скажет Django, что views.post_list — 
это правильное направление для запроса к твоему 
веб-сайту по адресу 
'http://127.0.0.1:8000/'.
name='post_list' (название представления) — 
это имя URL, которое будет 
использовано, чтобы идентифицировать его.
(?P<pk>\d+) — эта часть посложнее. Она означает, что Django возьмёт всё, что придется на эту часть строки, 
и передаст представлению в качестве переменной pk (обрати внимание, что её имя соответствуем имени переменной, 
используемой в качестве первичного ключа в файле blog/templates/blog/post_list.html). \d+ означает, что допустимы 
только цифры (от 0 до 9), но не буквы. + означает, что цифр должно быть одна или более. Таким образом, адрес 
http://127.0.0.1:8000/post// будет недействительным, а http://127.0.0.1:8000/post/1234567890/ совершенно правильным!

'''