from django.urls import path
from accounts import views
from .views import profile_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("accounts/create/", views.UserCreateAPIView.as_view(), name="account_create"),
    # Read, Update, Delete
    path("api/accounts/", views.UserListAPIView.as_view(), name="accounts_list"),
    path("api/accounts/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="account_rud"),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]
