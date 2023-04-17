from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from photography.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_admin = request.POST.get('is_admin')

        # create a new user object
        user = User(username=username, email=email, password=password, is_admin=is_admin)
        user.save()

        # return a JSON response indicating success
        return JsonResponse({'success': True})
    
class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful.'})
        else:
            return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
