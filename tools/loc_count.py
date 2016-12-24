import fnmatch
import os


def Walk(root='.', recurse=True, pattern='*'):
    """
        Generator for walking a directory tree.
        Starts at specified root folder, returning files
        that match our pattern. Optionally will also
        recurse through sub-folders.
    """
    for path, subdirs, files in os.walk(root):
        for name in files:
            if ".cs" in name:
                # print(name)
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
        if not recurse:
            break


def LOC(root='', recurse=True):
    """
        Counts lines of code in two ways:
            maximal size (source LOC) with blank lines and comments
            minimal size (logical LOC) stripping same

        Sums all Python files in the specified folder.
        By default recurses through subfolders.
    """
    count_mini, count_maxi = 0, 0
    for fspec in Walk(root, recurse, '*.cs'):
        skip = False
        for line in open(fspec).readlines():
            count_maxi += 1

            line = line.strip()
            if line:
                if line.startswith('#'):
                    continue
                if line.startswith('/'):  # ignore comments
                    continue
                if line.startswith('"""'):
                    skip = not skip
                    continue
                if not skip:
                    count_mini += 1

    return count_mini, count_maxi


if __name__ == '__main__':
    print(LOC(r"C:\Users\steffen.schneider\Desktop\web-testing\rms-web-testing\RMS-WebTesting-NUnit"))
    print(LOC(r"C:\Users\steffen.schneider\Desktop\web-testing\rms-web-testing\SeleniumRMSFunctions"))
