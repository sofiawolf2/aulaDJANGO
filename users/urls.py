from django.urls import path
from users.views import UserListView, UserLoginViews, UserLogoutView, UserCadastroView


app_name = 'users'

urlpatterns = [
    path('list',UserListView.as_view(),name = 'list_users'),
    path('login',UserLoginViews.as_view(),name = 'login_user'),
    path('logout',UserLogoutView.as_view(),name = 'logout_user'),   
    path('cadastro',UserCadastroView.as_view(),name = 'cadastro_user')

]

