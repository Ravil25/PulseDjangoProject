from django.urls import path
from rest_framework import routers
from .api import UserViewSet
from .views import add_user, ShowInfo, index, LoginUser, logout_user, AddReport

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls + [
    path('index', index.as_view(), name="index"),
    path('add_user/', add_user, name="add_user"),
    path('show_info/', ShowInfo.as_view(), name="show_info"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name='logout'),
    path('add_report/', AddReport.as_view(), name='add_report'),
    # path('contact/', AddReport.as_view(), name='contact'),
]
