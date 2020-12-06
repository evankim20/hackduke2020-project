from django.shortcuts import render, redirect
# from .utils import search_yt
from youtube_data.search import youtube_search
# Create your views here.

def landing_view(request):
    print('called landing')
    return render(request, 'landing.html')

def feed_view(request):
    temp_list = [{'video': 'video 1', 'teacher': 't1', 'stars': 5}, {'video': 'video 2', 'teacher': 't2', 'stars': 4},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}, {'video': 'video 3', 'teacher': 't3', 'stars': 3},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}, {'video': 'video 3', 'teacher': 't3', 'stars': 3},
                 {'video': 'video 3', 'teacher': 't3', 'stars': 3}]
    context = {'entries': temp_list}
    return render(request, 'feed.html', context)

def entry_view(request):
    context = {'video': {'title': 'User Registration and Login Authentication | Django (3.0) Crash Course Tutorials (pt 14)', 'teacher': 'Dennis Ivy', 'stars': 2.6},
               'reviews': [{'name': 'Bob', 'stars': 4, 'response': 'Great video!'}, {'name': 'Alice', 'stars': 1, 'response': 'Video sucked'},
                           {'name': 'Karen', 'stars': 3, 'response': 'meh'}]}
    return render(request, 'entry.html', context)

"""
insert_view handles the form POST request
"""
def insert_view(request):
    if request.POST:
        video_rating = request.POST.get('videorating')
        teacher_rating = request.POST.get('teacherrating')
        review = request.POST.get('review')

        # TODO: post to db and then redirect w/ updated info! (just grab from db again)
        print(f'Stuff: {video_rating}, {teacher_rating}, {review}')
        return redirect('entry')
    else:
        print("FAIL")
    return render(request, 'entry.html')

def search_view(request):
    if request.POST:
        search_query = request.POST.get('search_query')

        youtube_search(search_query, 5)

        # TODO: run search algorithm and return the list of video objects
        # get youtube search
        # create video object
        # put into context.videos

        # TODO: assign fake star ratings
        context = {'videos': []}

        return render(request, 'feed.html', context)

def watch_view(request):
    context = {}

    video_id = 'UmljXZIypDc'

    context['vid_url'] = video_id
    return render(request, 'common/watch.html', context)


