from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='inicio'),
    path('bienvenida',views.bienvenida),    
    path('bienvenida/<str:nombre>',views.bienvenida),
    path('turnos/',views.turnos,name='turnos'),
    path('login/',views.login,name='login'),
    path('registro/',views.registro,name='registro'),
    path('libro_de_quejas/',views.libro_de_quejas,name='libro_de_quejas'),
    #mapa
    path('donde_estamos/',views.donde_estamos,name='donde_estamos'),
    path('donde_estamos_caba/',views.donde_estamos_caba,name='donde_estamos_caba'),
    path('donde_estamos_washington/',views.donde_estamos_washington,name='donde_estamos_washington'),
    #Faq
    path("faq/", views.FaqView.as_view(), name="faq"),
    path("<str:pk>/detail/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    #institucional
    path("institucional/", views.institucional, name="institucional"),
    #noticia
    path('noticias/', views.noticias, name='noticias'),
    #path('noticias/<int:pk>/', views.noticias_detalle, name='noticias_detalle'),
    #path('noticia_nueva/', views.noticia_nueva, name='noticia_nueva'),
    #path('noticia/<int:pk>/edit/', views.noticia_edit, name='noticia_edit'),
]
