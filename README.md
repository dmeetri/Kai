# Kai
Voice assistant. Control your PC with voice commands

## Download VOSK
Download the vosk model from here: https://alphacephei.com/vosk/models
I used the Russian model: [vosk-model-ru-0.10] 2.5G https://alphacephei.com/vosk/models/vosk-model-ru-0.10.zip
Create a kai-desc/vosk-model folder and extract the downloaded archive there

## patch for fasttext if it throws an error:
1. open <venv>/lib/python3.12/site-packages/fasttext/FastText.py
2. find the line - return labels, np.array(probs, copy=False)
3. replace it with one of the following options: return labels, np.asarray(probs) | return labels, np.array(probs)

## Console commands