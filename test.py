import whisper
import numpy as np

model = whisper.load_model("large")
result = model.transcribe("Marco.m4a")
print(result["text"])
with open("transcription_Marco.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])



