from django.urls import path
from .views import index_view,ResumeScreeningAPI

urlpatterns = [
    path('screen/', ResumeScreeningAPI.as_view(), name='screen-resumes'),
    path('', index_view, name='index'),
]