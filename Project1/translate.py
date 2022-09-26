#Using Translate Library

from translate import Translator

translator = Translator(from_lang='english', to_lang='arabic')
translation = translator.translate('What is your name?')
print(translation)