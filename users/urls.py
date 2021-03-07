from django.urls import path
from . import views
from .views import Home, MenuOstad,OstadTamrin,VideoOstad,VideoOstadDetail,CreateVideo,OstadDetailTamrin,OstadCreateTamrin,OstadUpdateTamrin,TamrinCorrection,MenuStudent,StudentTamrin, UploadAnswer, VideoStudent, VideoDetailStudent, LoginPage, LogoutUser, RegisterPage




urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('menu_ostad/', MenuOstad.as_view(), name='menu_ostad'),
    path('menu_ostad/tamrin/', OstadTamrin.as_view(), name='tamrin_ostad'),
    path('menu_ostad/videos/', VideoOstad.as_view(), name='video_ostad'),
    path('menu_ostad/videos/<int:video_id>', VideoOstadDetail.as_view(), name='video_detail_ostad'),
    path('menu_ostad/create_video/', CreateVideo.as_view(), name='create_video'),
    path('menu_ostad/tamrin/<int:tamrin_id>/', OstadDetailTamrin.as_view(), name='detail_tamrin_ostad'),
    path('menu_ostad/createTamrin', OstadCreateTamrin.as_view(), name='create_tamrin'),
    path('menu_ostad/updateTamrin/<int:pk>', OstadUpdateTamrin.as_view(), name='update_tamrin'),
    path('menu_ostad/tamrin/correction/<int:answer_id>', TamrinCorrection.as_view(), name='tamrin_detail_ostad_correction'),

    path('menu_student/', MenuStudent.as_view(), name='menu_student'),
    path('menu_student/tamrin/', StudentTamrin.as_view(), name='tamrin_student'),
    path('menu_student/tamrin/upload/<int:tamrin_id>', UploadAnswer.as_view(), name='upload_answer'),
    path('menu_student/videos', VideoStudent.as_view(), name='video_student'),
    path('menu_student/videos/<int:video_id>', VideoDetailStudent.as_view(), name='detail_video_ostad'),

    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),


]
