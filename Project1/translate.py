## Tranlating word to another language using Translate Library

from translate import Translator

translator = Translator(from_lang='english', to_lang='spanish')
translation = translator.translate('What is your name?')
print(translation)