from django.conf.urls import url
from users.views import RegisterView, LoginView, LogoutView, IndexView, HighApplyView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
	url(r'^highapply/$', HighApplyView.as_view(), name='highapply'),
]