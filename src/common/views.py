from django.shortcuts import render

# Create your views here.

def landing_view(request):
    print('called landing')
    return render(request, 'landing.html')

def feed_view(request):
    temp_list = ["Video 1", "Video 2", "Video 3"]
    context = {'entries': temp_list}
    return render(request, 'feed.html', context)

def entry_view(request):
    temp_list = ["Review 1", "Review 2", "Review 3"]
    context = {'reviews': temp_list}
    return render(request, 'entry.html', context)