from gtts import gTTS

text = "혼저옵서예. 뭐햄수과"
tts = gTTS(text=text, lang="ko")
filename = "media/tts/voice.mp3"
tts.save(filename)