import torch
import time

language = 'ru'
model_id = 'v3_1_ru' # другая версия русского
sample_rate = 48000
speaker = 'aidar'
put_accent = True
put_yo = True


device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id,
                                     trust_repo=True) # <- доверяем репозиторию

model.to(device)

def say(text: str):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    import sounddevice as sd
    sd.play(audio, sample_rate)
    time.sleep((len(audio) / sample_rate)+1)
    sd.stop()
