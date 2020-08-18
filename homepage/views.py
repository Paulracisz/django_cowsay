import subprocess
from django.shortcuts import render
from homepage import models
from homepage.forms import AddCow

# Create your views here.

def index(request):
    if request.method == "POST":
        cow_speech = AddCow(request.POST)
        if cow_speech.is_valid():
            data = cow_speech.cleaned_data
            user_text = data.get("user_input")
            models.CowSpeech.objects.create(
                user_text = user_text,
            )
            cowsaid = subprocess.run(f'cowsay "{user_text}"', capture_output=True, shell=True, ).stdout.decode('utf-8')
            return render(request, "index.html", {"cow_speech": cow_speech, "Welcome": "Welcome to the Cow Speech!", "subprocess": cowsaid,})
    cow_speech = AddCow()
    return render(request, "index.html", {"cow_speech": cow_speech, "Welcome": "Welcome to the Cow Speech!"})

def history(request):
    history_text = models.CowSpeech.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {"history_text": history_text, "Top_10": "Top 10 Most Recent Inputs!"})