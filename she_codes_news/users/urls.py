from django.urls import path
from .views import CreateAccountView, ViewAccount

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', ViewAccount.as_view(), name='viewAccount')
    # path('fav/<int:pk>/', views.favourite_add, name='favourite-add'),
]