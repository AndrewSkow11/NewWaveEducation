from django.urls import path
from accounts import views

urlpatterns = [
    path("accounts/create/", views.UserCreateAPIView.as_view(), name="account_create"),
    # Read, Update, Delete
    path("api/accounts/", views.UserListAPIView.as_view(), name="accounts_list"),
    path("api/accounts/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="account_rud"),
]
