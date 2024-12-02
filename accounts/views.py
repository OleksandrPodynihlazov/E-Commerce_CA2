from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from .models import CustomUser

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('shop:cat_list')
    
    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)
        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)
        # Log the user in after signup
        login(self.request, self.object)
        return response # Redirect to success URL
    
def edit_profile(request):
    user = request.user  
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)  
        if form.is_valid():
            form.save() 
            return redirect('accounts:profile') 
        else:
            
            print(form.errors)
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})

def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})


