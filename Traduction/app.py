# coding= UTF-8

import translate
from translate import Translator 

data  = Translator(from_lang="fr", to_lang="en")
res  = data.translate("salut je suis ahmed boukhriss filai")

print(res)