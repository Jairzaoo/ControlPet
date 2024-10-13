from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def login_redirect(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')  # Redirect to your home page instead of the login page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
