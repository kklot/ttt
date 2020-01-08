from django.urls import path

from . import views

app_name = 'check'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.Qlist.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('', views.get_tt, name='index'),
    path('ketqua_tt/', views.ketqua_tt, name='ketqua_tt'),
    path('<int:pk>/', views.Qdetail.as_view(), name='detail'),
    path('<int:pk>/results/', views.Vresult.as_view(), name='results'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]