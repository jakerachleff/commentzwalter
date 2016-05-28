import pathlib

TEST_FILE = "corpus/text1"
CORPUS = "corpus/"
N_SHINGLES = 100


def get_shingles(text, k):
	"""Return a list of the k-singles of a text file

	@param text: string to convert to shingles
    @param k: length of each single
    @return: list of shingles
    """
	return [text[i:i+k] for i in range(len(text))]
    
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

    for file_name in file_names:
	    text = ''.join([line.rstrip('\n') for line in open(file_name)])
	    shingles = get_shingles(text, N_SHINGLES)





