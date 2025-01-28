from django.shortcuts import render

def swap_view(request):
    return render(request, 'swap.html')
