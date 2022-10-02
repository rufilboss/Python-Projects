# Tranlating word to another language using Goslate Library
import goslate

insert_word = input('Enter what you want to translate:....')

trans_df = goslate.Goslate()
trans_df.translate(insert_word, 'fr')

