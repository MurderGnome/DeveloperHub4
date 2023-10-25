from django.urls import path
from .views import learning_outcomes_view, lesson_plans_view # ... Add other views ...

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    path('learning_outcomes/<int:project_id>/', learning_outcomes_view, name='learning_outcomes'),
    path('lesson_plans/<int:learning_outcome_id>/', lesson_plans_view, name='lesson_plans'),
    # ... Add other paths ...
]
# urls.py in the content_generation app or the relevant app

from django.urls import path
from . import views

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    ...
    path('pdf/<int:project_id>/', views.ProjectPDFView.as_view(), name='project_pdf'),
    ...
]

# urls.py in the content_generation app or the relevant app

from django.urls import path
from . import views

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    ...
    path('share/<int:project_id>/', views.share_project, name='share_project'),
    ...
]

# urls.py in the content_generation app or the relevant app

from django.urls import path
from . import views

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    ...
    path('autosave/<int:project_id>/', views.auto_save_project, name='auto_save_project'),
    ...
]

# urls.py in the content_generation app or the relevant app

from django.urls import path
from . import views

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    ...
    path('view-by-id/', views.view_project_by_id, name='view_project_by_id'),
    ...
]

# urls.py in the content_generation app or the relevant app

from .views import LearningOutcomeCreateView, LearningOutcomeListView

urlpatterns = [
    path('firebase_logout/', views.firebase_logout_endpoint, name='firebase_logout'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('handle_firebase_login/', views.handle_firebase_login_endpoint, name='handle_firebase_login'),
    path('signup/', views.firebase_signup_view, name='firebase_signup'),
    path('login/', views.firebase_login_view, name='firebase_login'),
    ...
    path('add-outcome/', LearningOutcomeCreateView.as_view(), name='add_outcome'),
    path('outcomes/', LearningOutcomeListView.as_view(), name='learning_outcome_list'),
    ...
]

    path('password_reset/', views.password_reset_request, name='password_reset_request'),
