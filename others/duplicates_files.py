"""
Dropbox

Question: Given root directory, search all directories and return duplicate files
input: root path
output: list[list[]]
"""

import os
import collections

###
# Helper class to abstract language io implementation differences
class PathHelper:
    @staticmethod
    def is_file(abs_path):
        return os.path.isfile(abs_path)

    @staticmethod
    def is_dirctory(abs_path):
        return os.path.isdir(abs_path)

    @staticmethod
    def get_file_paths(abs_path):
        if PathHelper.is_dirctory(abs_path):
            return os.listdir(abs_path)

    @staticmethod
    def get_file_hash(file_path):
        '''
        generate hash of file content
        You can use any hash or message digestion algorithm, i.e. md5, sha1
        here, I just use simple python builtin hash function
        '''
        h = hash(open(file_path).read())


class Solution:
    def find_duplicates_bfs(self, root):
        '''
        Main algorithm
        Iterate through all directories
        hash each file and keep existing file hashs
        '''
        existing_file_hashs = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)

        while queue:
            curt_path = queue.popleft()
            paths = PathHelper.get_file_paths()
            for p in paths:
                if PathHelper.is_dirctory(p):
                    queue.append(p)
                elif PathHelper.is_file(p):
                    file_hash = PathHelper.get_file_hash(p)
                    existing_file_hashs[file_hash].append(p)

        # only return files that has same hash(same content file)
        duplicates = []
        for hash_val, files in existing_file_hashs.items():
            if len(files) > 1:
                duplicates.append(files)
        return duplicates
