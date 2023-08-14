from django.shortcuts import redirect,render


# to check if the user is logged in or out

def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args,**kwargs )
    return wrapper_function
    
    #give access to admin if request comes from admin page
def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function
    
def user_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return redirect('/dashboard')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function