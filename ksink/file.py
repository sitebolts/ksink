#https://stackoverflow.com/a/9824894/1741346
def save_file(file):
    file.flush()
    os.fsync(file.fileno())
