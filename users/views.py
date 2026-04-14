from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'balance': request.user.balance})


from django.shortcuts import render

# Create your views here.
