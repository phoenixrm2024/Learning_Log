from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

"""Defines URL patterns for learning_logs."""
# Home page
def index(request):                                     # Original request object
    return render(request, 'learning_logs/index.html')  # 'app folder/index.html'

# Page shows all topics
@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # Instance of class Topic
    context = {'topics': topics}  
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)            # topic_id; a parameter that store its value received from URL.
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added') # minus(-); sort in reverse
    context = {'topic': topic, 'entries': entries}    # template context; keys as costs. & values as vars.
    return render(request, 'learning_logs/topic.html', context)
@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':                # So the request is probably "GET" request method
    # No data submitted; create a blank form.
        form = TopicForm()
    else:
    # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
@login_required 
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic= Topic.objects.get(id=topic_id)
    if request.method != 'POST':                # So the request is probably "GET" request method
    # No data submitted; create a blank form.
        form = EntryForm()
    else:
    # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic,'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """Add a new entry for a particular topic."""
    entry= Entry.objects.get(id=entry_id)
    topic = entry.topic
        # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':            # So the request is probably "GET" request method
    # No data submitted; create a blank form.
        form = EntryForm(instance=entry)    # Making an instance of EntryForm with the argument instance=entry
    else:
    # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    # Display a blank or invalid form.
    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

