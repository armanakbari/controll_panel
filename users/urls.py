from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('menu_ostad/', views.menuOstad, name='menu_ostad'),
    path('menu_ostad/tamrin/', views.ostadTamrin, name='tamrin_ostad'),
    path('menu_ostad/videos/', views.videoOstad, name='video_ostad'),
    path('menu_ostad/videos/<int:video_id>', views.videoOstadDetail, name='video_detail_ostad'),
    path('menu_ostad/create_video/', views.createVideo, name='create_video'),
    path('menu_ostad/tamrin/<int:tamrin_id>/', views.ostadDetailTamrin, name='detail_tamrin_ostad'),
    path('menu_ostad/createTamrin', views.ostadCreateTamrin, name='create_tamrin'),
    path('menu_ostad/updateTamrin/<int:pk>', views.ostadUpdateTamrin, name='update_tamrin'),
    path('menu_ostad/tamrin/correction/<int:answer_id>', views.tamrinCorrection, name='tamrin_detail_ostad_correction'),

    path('menu_student/', views.menuStudent, name='menu_student'),
    path('menu_student/tamrin/', views.studentTamrin, name='tamrin_student'),
    path('menu_student/tamrin/upload/', views.uploadAnswer, name='upload_answer'),
    path('menu_student/videos', views.videoStudent, name='video_student'),
    path('menu_student/videos/<int:video_id>', views.videoDetailStudent, name='detail_video_ostad'),



    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
]
