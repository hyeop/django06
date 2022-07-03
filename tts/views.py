from django.shortcuts import render
from gtts import gTTS



# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        bf = request.POST.get("bf")
        fn = request.POST.get("fname")
        la = request.POST.get("lang")
        print(bf, fn, la)
        tts = gTTS(text=bf, lang=la)
        filename = f"media/tts/{fn}.mp3"
        tts.save(filename)
        context = {
            "bf":bf,
            "fn":fn,
            "la":la
        }
    return render(request, "tts/index.html", context)
