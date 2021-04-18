#Convert a string like 'best-toasters_2021' to a string like 'best toasters 2021'
def convert_url_path_to_words(url_path):
    cleaned_url_path = url_path.replace('/', ' ').replace('-', ' ').replace('_', ' ')
    cleaned_url_path = cleaned_url_path.strip()
    cleaned_url_path = ' '.join(cleaned_url_path.split()) #Remove any double spaces
    return cleaned_url_path
