from django.contrib import admin
from django.urls import path, include
from user_profiles.views import login_view
from user_profiles import views
# Import the login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_profiles/', include('user_profiles.urls')),  # Fixed this line
    path('', login_view, name='login_view'),  # Direct root URL to login_view
    path('signup/', views.signup_view, name='signup_view'),
]
