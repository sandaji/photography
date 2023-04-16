from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from photography.models import User

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
