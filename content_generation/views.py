
from django.shortcuts import render, redirect
from .models import Course, Module, STSLineItem, LearningOutcome
from user_profiles.models import UserProfile

def dashboard_view(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'content_generation/dashboard.html', {'courses': courses})

def course_creation_view(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(user=request.user)
        course_name = request.POST.get('course_name')
        course_dev_manager = request.POST.get('course_development_manager_name')
        new_course = Course.objects.create(user=user, course_name=course_name, course_development_manager_name=course_dev_manager)

        module_count = 1
        while f'module_name_{module_count}' in request.POST:
            module_name = request.POST.get(f'module_name_{module_count}')
            new_module = Module.objects.create(course=new_course, module_name=module_name)

            sts_count = 1
            while f'sts_item_name_{module_count}_{sts_count}' in request.POST:
                sts_name = request.POST.get(f'sts_item_name_{module_count}_{sts_count}')
                new_sts_item = STSLineItem.objects.create(module=new_module, sts_item_name=sts_name)

                learning_outcome_count = 1
                while f'learning_outcome_{module_count}_{sts_count}_{learning_outcome_count}' in request.POST:
                    learning_outcome_desc = request.POST.get(f'learning_outcome_{module_count}_{sts_count}_{learning_outcome_count}')
                    LearningOutcome.objects.create(sts_line_item=new_sts_item, description=learning_outcome_desc)
                    learning_outcome_count += 1

                sts_count += 1

            module_count += 1

        return redirect('dashboard')

    return render(request, 'content_generation/course_creation.html')


def firebase_signup_view(request):
    return render(request, 'firebase_signup.html')

def firebase_login_view(request):
    return render(request, 'firebase_login.html')


from django.contrib.auth.models import User
from django.contrib.auth import login, logout

def handle_firebase_authentication(request, id_token):
    """Handle user session in Django based on Firebase authentication."""
    # Verify the Firebase ID token and get the user's email
    user_email = verify_firebase_token(id_token)
    if user_email:
        # Find or create a Django user with the verified email
        user, _ = User.objects.get_or_create(username=user_email, email=user_email)
        # Log the user in
        login(request, user)
        return True
    return False

def firebase_logout(request):
    """Log the user out from Django."""
    logout(request)
    # Redirect to login page or any other page as desired
    return redirect('/login/')



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def handle_firebase_login_endpoint(request):
    """Handle the received Firebase ID token from the frontend."""
    if request.method == 'POST':
        data = json.loads(request.body)
        id_token = data.get('token')
        if handle_firebase_authentication(request, id_token):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'method not allowed'}, status=405)



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def handle_firebase_login_endpoint(request):
    """Endpoint to handle Firebase login and manage Django user session."""
    if request.method == 'POST':
        data = json.loads(request.body)
        id_token = data.get('token')
        if handle_firebase_authentication(request, id_token):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'method not allowed'}, status=405)



@csrf_exempt
def firebase_logout_endpoint(request):
    """Endpoint to handle Firebase logout and end Django user session."""
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'method not allowed'}, status=405)


from firebase_admin import firestore

def add_course_to_firestore(course_name, course_manager):
    """Add a new course to the 'courses' collection in Firestore."""
    db = firestore.client()
    courses_ref = db.collection('courses')
    course_data = {
        'name': course_name,
        'manager': course_manager,
        'created': firestore.SERVER_TIMESTAMP
    }
    courses_ref.add(course_data)

# Example usage:
# add_course_to_firestore('Math 101', 'John Doe')

def create_course(course_name, course_manager, user_email):
    """Create a new course in the 'courses' collection in Firestore."""
    db = firestore.client()
    courses_ref = db.collection('courses')
    course_data = {
        'name': course_name,
        'manager': course_manager,
        'user_email': user_email,
        'created': firestore.SERVER_TIMESTAMP
    }
    courses_ref.add(course_data)

# Example usage:
# create_course('Math 102', 'Jane Doe', 'jane.doe@example.com')

def get_courses_for_user(user_email):
    """Retrieve a list of courses for a specific user from Firestore."""
    db = firestore.client()
    courses_ref = db.collection('courses')
    courses_query = courses_ref.where('user_email', '==', user_email)
    courses = courses_query.stream()
    return [{'id': course.id, **course.to_dict()} for course in courses]

# Example usage:
# courses_list = get_courses_for_user('jane.doe@example.com')

def update_course(course_id, updated_course_name, updated_course_manager):
    """Update an existing course's details in Firestore based on the course's document ID."""
    db = firestore.client()
    course_ref = db.collection('courses').document(course_id)
    updated_data = {
        'name': updated_course_name,
        'manager': updated_course_manager
    }
    course_ref.update(updated_data)

# Example usage:
# update_course('some_document_id', 'Updated Math 102', 'Updated Jane Doe')

def delete_course(course_id):
    """Delete a course from Firestore based on the course's document ID."""
    db = firestore.client()
    course_ref = db.collection('courses').document(course_id)
    course_ref.delete()

# Example usage:
# delete_course('some_document_id')

from django.shortcuts import render

def list_courses(request):
    """View to display a list of courses for the logged-in user."""
    user_email = request.user.email
    courses = get_courses_for_user(user_email)
    return render(request, 'list_courses.html', {'courses': courses})


def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # TODO: Integrate with Firebase to send password reset email
        # Placeholder logic for Firebase integration:
        # firebase_auth.send_password_reset_email(email)
        messages.success(request, 'Password reset link has been sent to your email.')
        return redirect('login_view')
    return render(request, 'registration/password_reset_request.html')

def create_module_view(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            # TODO: Associate the module with a specific course, e.g., module.course = some_course
            module.save()
            messages.success(request, 'Module created successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after creation
    else:
        form = ModuleForm()
    return render(request, 'content_generation/module_form.html', {'form': form})

def update_module_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module updated successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after updating
    else:
        form = ModuleForm(instance=module)
    return render(request, 'content_generation/module_form.html', {'form': form})

def delete_module_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        module.delete()
        messages.success(request, 'Module deleted successfully!')
        return redirect('dashboard')  # Redirect to a suitable view after deletion
    return render(request, 'content_generation/module_confirm_delete.html', {'module': module})

def create_sts_line_item_view(request):
    if request.method == 'POST':
        form = STSLineItemForm(request.POST)
        if form.is_valid():
            sts_line_item = form.save(commit=False)
            # TODO: Associate the sts_line_item with a specific module, e.g., sts_line_item.module = some_module
            sts_line_item.save()
            messages.success(request, 'STS Line Item created successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after creation
    else:
        form = STSLineItemForm()
    return render(request, 'content_generation/sts_line_item_form.html', {'form': form})

def update_sts_line_item_view(request, sts_line_item_id):
    sts_line_item = get_object_or_404(STSLineItem, id=sts_line_item_id)
    if request.method == 'POST':
        form = STSLineItemForm(request.POST, instance=sts_line_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'STS Line Item updated successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after updating
    else:
        form = STSLineItemForm(instance=sts_line_item)
    return render(request, 'content_generation/sts_line_item_form.html', {'form': form})

def delete_sts_line_item_view(request, sts_line_item_id):
    sts_line_item = get_object_or_404(STSLineItem, id=sts_line_item_id)
    if request.method == 'POST':
        sts_line_item.delete()
        messages.success(request, 'STS Line Item deleted successfully!')
        return redirect('dashboard')  # Redirect to a suitable view after deletion
    return render(request, 'content_generation/sts_line_item_confirm_delete.html', {'sts_line_item': sts_line_item})

def update_sts_line_item_view(request, sts_line_item_id):
    sts_line_item = get_object_or_404(STSLineItem, id=sts_line_item_id)
    if request.method == 'POST':
        form = STSLineItemForm(request.POST, instance=sts_line_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'STS Line Item updated successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after updating
    else:
        form = STSLineItemForm(instance=sts_line_item)
    return render(request, 'content_generation/sts_line_item_form.html', {'form': form})

def delete_sts_line_item_view(request, sts_line_item_id):
    sts_line_item = get_object_or_404(STSLineItem, id=sts_line_item_id)
    if request.method == 'POST':
        sts_line_item.delete()
        messages.success(request, 'STS Line Item deleted successfully!')
        return redirect('dashboard')  # Redirect to a suitable view after deletion
    return render(request, 'content_generation/sts_line_item_confirm_delete.html', {'sts_line_item': sts_line_item})

def create_learning_outcome_view(request):
    if request.method == 'POST':
        form = LearningOutcomeForm(request.POST)
        if form.is_valid():
            learning_outcome = form.save(commit=False)
            # TODO: Associate the learning_outcome with a specific STSLineItem, e.g., learning_outcome.sts_line_item = some_sts_line_item
            learning_outcome.save()
            messages.success(request, 'Learning Outcome created successfully!')
            return redirect('dashboard')  # Redirect to a suitable view after creation
    else:
        form = LearningOutcomeForm()
    return render(request, 'content_generation/learning_outcome_form.html', {'form': form})
