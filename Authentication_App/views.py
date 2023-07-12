# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from coreApp.forms import TenantRegistrationForm

# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = TenantRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = TenantRegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})
