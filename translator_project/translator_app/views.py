from django.shortcuts import render
from googletrans import Translator

def translate_word(request):
    translated_text = ''
    source_text = ''
    target_language = 'en'

    if request.method == 'POST':
        source_text = request.POST['source_text']
        target_language = request.POST['target_language']

        translator = Translator()
        translation = translator.translate(source_text, dest=target_language)
        translated_text = translation.text

    return render(request, 'translator_app/translate.html', {
        'source_text': source_text,
        'target_language': target_language,
        'translated_text': translated_text,
    })
