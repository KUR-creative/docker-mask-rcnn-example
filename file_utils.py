'''
Utils for File Processing
'''
import os
from pathlib import PurePosixPath, Path

def children(dirpath):
    ''' Return children file path list of `dirpath` '''
    parent = Path(dirpath)
    return list(map(
        lambda child_path: str(parent / child_path.name),
        parent.iterdir()
    ))

def identity(x): return x
def pathseq(root, pred=identity, f=str):
    ''' List all the file paths in root, recursively. 
    pred to filter the results, f to map the filtereds. 
    See https://github.com/KUR-creative/kur-blog/blob/f9747a6f65aaa1aaeb8f02a68a05f9aaf3f77099/src/clj/kur/util/file_system.clj#L33'''
    for curr, dirs, files in os.walk(root):
        for file in filter(pred, files):
            yield f(Path(curr) / file)