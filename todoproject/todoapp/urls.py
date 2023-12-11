from django.conf.urls.static import static
from django.urls import path

from todoapp import views, admin
from todoproject import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvhome/',views.tasklistview.as_view(),name="cbvhome"),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name="cbvudelete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
