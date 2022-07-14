from translate import Translator

# Configura a tradução #
s = Translator(from_lang="english", to_lang="pt-br")

# Traduz texto desejado #
resultado = s.translate("Hello World")

print('-' * 100)

print('Tradução: ' + resultado)