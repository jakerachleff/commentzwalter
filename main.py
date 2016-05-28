import pathlib

TEST_FILE = "corpus/text1"
CORPUS = "corpus/"

def files_in_directory(dirname):
    """CITATION: Taken from the starter code of a CS41 assignment

    Return a list of filenames in the given directory.

    @param dirname: name of directory from which to acquire files.
    @return: list of strings representing names of files in the given directory
    """
    p = pathlib.Path(dirname)
    if not p.is_dir():
        raise NotADirectoryError("`{d}` is not a directory".format(d=dirname))
    return [str(child) for child in p.iterdir() if child.is_file()]

if __name__ == '__main__':

    file_names = files_in_directory(CORPUS)

    #for file_name in file_names:
    file_name = file_names[0]
    lines = [line.rstrip('\n') for line in open(file_name)]
    text = ''.join(lines) 
    print(text)


