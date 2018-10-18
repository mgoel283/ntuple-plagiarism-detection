"""
plagiarism_detection.py

Manav Goel
"""


class PlagDetect(object):
    """
    Class that implements functions needed to check for plagiarism
    """

    DEFAULT_TUPLE_LEN = 3

    def __init__(self, syn_file, file_1, file_2, tuple_len=DEFAULT_TUPLE_LEN):
        self.tuple_len = tuple_len
        self.syn_map = self.syn_hash(syn_file)
        self.source_dict = self.tuple_list_dict(file_2, 1)
        self.target_list = self.tuple_list_dict(file_1, 0)

    def syn_hash(self, in_file):
        """
        Creates a hash table of synonyms with the first word being the value
        :return: dict of synonyms
        """
        syn_hashmap = {}
        with open(in_file, 'r') as syn_file:
            for line in syn_file:
                syns = line.split()
                default_syn = syns[0]
                for index in range(1, len(syns)):
                    syn_hashmap[syns[index]] = default_syn

        return syn_hashmap

    def tuple_list_dict(self, in_file, want_dict):
        """
        """
        my_tuple = []

        if want_dict:
            tuple_struct = {}
        else:
            tuple_struct = []

        with open(in_file, 'r') as my_file:
            for line in my_file:
                words = line.split()
                for word in words:
                    word = self.word_to_syn(word)  # converts synonyms
                    if len(my_tuple) == self.tuple_len:
                        my_tuple.pop(0)
                        my_tuple.append(word)
                        if want_dict:
                            tuple_struct[tuple(my_tuple)] = True
                        else:
                            tuple_struct.append(tuple(my_tuple))
                    else:
                        my_tuple.append(word)
                        if (len(my_tuple) == self.tuple_len) and want_dict:
                            tuple_struct[tuple(my_tuple)] = True
                        elif (len(my_tuple) == self.tuple_len) and not want_dict:
                            tuple_struct.append(tuple(my_tuple))
        print(tuple_struct)
        return tuple_struct

    def word_to_syn(self, word):
        if word in self.syn_map:
            word = self.syn_map[word]

        return word

    def plag_percent(self):
        """
        """

        total_tuples = len(self.target_list)
        if total_tuples == 0:
            return 0

        plag_tuples = 0  # count of plagiarized tuples
        for tuple in self.target_list:
            if tuple in self.source_dict:
                plag_tuples += 1

        return (float(plag_tuples)/float(total_tuples)) * 100
        #return plag_tuples
