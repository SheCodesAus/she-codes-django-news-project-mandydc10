from django.urls import path
from .views import CreateAccountView, ViewAccount, UpdateAccount

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', ViewAccount.as_view(), name='viewAccount'),
    path('create-account/edit', UpdateAccount.as_view(), name='updateAccount'),
    path('profile/<int:pk>/', ViewAccount.as_view(), name='profile'),
    # path('fav/<int:pk>/', views.favourite_add, name='favourite-add'),
]