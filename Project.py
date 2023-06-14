#!pip install deep-translator
import pandas as pd
import numpy as np
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)

languages =['de', 'en']
text = input('What text would you like to translate? ')
data = {'other_language': ['eten', 'mencari', 'arm', 'genomen']}  
df = pd.DataFrame(data)  
 
for language in languages:
deep_translator = GoogleTranslator(source='de', target='en') 
df['translated_value'] = df['other_language'].apply(lambda x: translator.translate(x))
print(f'{language}: {translator.translate}')