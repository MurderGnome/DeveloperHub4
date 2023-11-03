import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class FirebaseAuthenticationBackend(BaseBackend):
    def authenticate(self, request, firebase_token=None, **kwargs):
        # Initialize Firebase Admin SDK if not already initialized
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate('path_to_your_firebase_credentials.json')  # Replace with the path to your Firebase credentials
            firebase_admin.initialize_app(cred)

        # Verify the token with Firebase
        decoded_token = auth.verify_id_token(firebase_token)
        firebase_uid = decoded_token.get("uid")

        if not firebase_uid:
            return None

        # Get or create a Django user
        user, created = User.objects.get_or_create(username=firebase_uid)
        
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
