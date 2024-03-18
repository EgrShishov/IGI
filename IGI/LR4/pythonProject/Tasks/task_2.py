import re
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED


def read_from_file(path):
    with open(path, 'r') as file:
        try:
            data = file.readlines()
            file.close()
            return data
        except BaseException:
            print('Something went wrong!')
            return


def save_in_file(path, data):
    with open(path, 'w+') as file:
        try:
            file.writelines(data)
            file.close()
        except BaseException:
            print('Something went wrong!')
            return


def archive_file(filepath, path_to_zip):
    with ZipFile(path_to_zip, 'w', compression=ZIP_DEFLATED, compresslevel=2) as zip:
        zip.write(filepath)


def get_archive_info(path_to_zip):
    with ZipFile(path_to_zip) as zip:
        for info in zip.infolist():
            print('Info about files:')
            if info.is_dir():
                print('Is folder')
            else:
                print('Is file')
            print(f'Size: {info.file_size}, name: {info.filename}, date: {info.date_time}')


def analyze_text(text: str):
    result_str = ""

    sentences_amount = len(re.findall(r'([.?!])', text))

    narrative = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    questions = [sentence for sentence in narrative if '?' in sentence]
    excl = [sentence for sentence in narrative if '!' in sentence]

    nar_amount = len(narrative)
    inter_amount = len(questions)
    excl_amount = len(excl)

    words = re.findall(r'\b[A-z]+\b', text)
    print(f'words: {words}')
    av_len = .0
    for word in words:
        av_len += len(word)
    av_len /= len(words)

    ave_sentence_len = 0

    result_str += (f'Amount of sentences in the text: {sentences_amount}\n') #
    result_str += (f'Amount of narrative. sentences in the text: {nar_amount}\n') #
    result_str += (f'Amount of interrogative? sentences in the text: {inter_amount}\n') #
    result_str += (f'Amount of exclamation! sentences in the text: {excl_amount}\n') #

    result_str += (f'Amount of words in text: {len(words)}\n')
    result_str += (f'Average length of words in sentences: {av_len}\n')
    result_str += (f'Average len of sentences in words: {ave_sentence_len}\n') #

    smiles = re.findall(r'( +([;:]){1}-*([()\]\[])+)', text)
    result_str += (f'Amount of smiles: {len(smiles)}\n')

    capital_letters = re.findall(r'[A-Z]', text)
    result_str += (f'All capital letters in text: {capital_letters}\n')

    count_less_5 = len(list(re.findall(r'\b[A-z]{1,4}\b', text)))
    result_str += (f'Amount of words, with less than 5 characters: {count_less_5}\n')

    shortest_words = list(re.findall(r'\b[A-z]+d\b', text))
    if len(shortest_words) != 0:
        shortest_words.sort(key=len)
        result_str += (f'The shortest word, which ends with "d": {shortest_words[0]}\n')
    else:
        result_str += (f'There are no words, which ends with "d"\n')

    words.sort(reverse=True, key=len)
    result_str += (f'All words, sorted in reverse len order : {words}\n')

    text = re.sub(r'(p*)(b+)(c*)', 'ddd', text) #fix later
    result_str += (f'Changed text: {text}\n')

    return result_str


def task2():
    original_path = 'text.txt'
    path_to_save = 'answer.txt'
    path_to_archive = 'archive.zip'
    file_data = str(read_from_file(original_path))
    result = analyze_text(file_data)
    save_in_file(path_to_save, result)
    archive_file(path_to_save, path_to_archive)
    get_archive_info(path_to_archive)

