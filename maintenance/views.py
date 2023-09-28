from django.shortcuts import render

from .forms import MaintenanceRequestForm

def maintenance_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            maintenance_request.requester = request.user  # Assuming you have user authentication
            maintenance_request.save()
            # form.save()
            # Redirect or display a success message
    else:
        form = MaintenanceRequestForm()

    context = {'form': form}
    return render(request, 'maintenance/maintenance_request.html', context)

