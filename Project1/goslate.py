# Using Goslate Library
from fnmatch import translate
import goslate

insert_text = "My name is Ilyas"

new_gs = goslate.Goslate()
print(new_gs.translate(insert_text, 'fr'))

