def convert_text(text):
    processed_text = text

    vocal = ['a', 'e', 'i', 'o', 'u', 'n']
    acentos = ['á', 'é', 'í', 'ó', 'ú', 'ñ']

    characteres = [',', '.', '!', '¡', '¿', '?', '-', ':', ';', '—', '»', '«', '(', ')']

    for char in characteres:
        processed_text = processed_text.replace(char, '')

    for i in range(len(acentos)):
        processed_text = processed_text.replace(acentos[i], vocal[i])

    processed_text = processed_text.replace("\n"," ")
    processed_text = processed_text.replace(" ","")
    processed_text = processed_text.upper()

    return processed_text

def process(path):
    file = open(path, 'r', encoding='utf-8')
    text = file.read()

    return convert_text(text)