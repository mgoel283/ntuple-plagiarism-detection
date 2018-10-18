"""
plagiarism_detection.py

Manav Goel
"""
import string


class PlagDetect(object):
    """
    Class that implements functions needed to check for plagiarism
    """

    DEFAULT_TUPLE_LEN = 3

    def __init__(self, syn_file, file_1, file_2, tuple_len=DEFAULT_TUPLE_LEN):
        """
        :param syn_file: File of synonyms
        :param file_1: Base file
        :param file_2: File checking for plagiarism
        :param tuple_len: (optional) tuple length
        """
        if int(tuple_len) <= 0:
            raise ValueError
        else:
            self.tuple_len = tuple_len
            self.syn_map = self.syn_hash(syn_file)
            self.source_dict = self.tuple_list_dict(file_2, 1)
            self.target_list = self.tuple_list_dict(file_1, 0)

    def syn_hash(self, in_file):
        """
        Returns a dictionary of the synonyms, with first word as the value
        :param in_file: Synonyms to be parsed
        :return: syn_hashmap: Dictionary of syns
        """
        syn_hashmap = {}
        with open(in_file, 'r') as syn_file:
            for line in syn_file:
                syns = line.split()
                default_syn = self.sanitize_word(syns[0])
                for index in range(1, len(syns)):  # add the synonyms to the dictionary
                    syn_hashmap[self.sanitize_word(syns[index])] = default_syn

        return syn_hashmap

    def tuple_list_dict(self, in_file, want_dict):
        """
        Generates a list or dictionary containing tuples from a file
        :param in_file: File to be parsed
        :param want_dict: Boolean for dictionary (1) or list(0)
        :return: tuple_struct: Either a list or dictionary of tuples
        """
        my_tuple = []  # holds a single tuple at a time

        if want_dict:
            tuple_struct = {}
        else:
            tuple_struct = []

        with open(in_file, 'r') as my_file:

            for line in my_file:
                words = line.split()

                for word in words:
                    word = self.word_to_syn(self.sanitize_word(word))  # converts synonyms
                    if len(my_tuple) == self.tuple_len:  # check if we have a full tuple
                        my_tuple.pop(0)  # replace the oldest word
                        my_tuple.append(word)

                        # add tuple to appropriate dict/list
                        if want_dict:
                            tuple_struct[tuple(my_tuple)] = True
                        else:
                            tuple_struct.append(tuple(my_tuple))

                    else:  # fill my_tuple until it reaches length tuple_len
                        my_tuple.append(word)

                        if (len(my_tuple) == self.tuple_len) and want_dict:
                            tuple_struct[tuple(my_tuple)] = True
                        elif (len(my_tuple) == self.tuple_len) and not want_dict:
                            tuple_struct.append(tuple(my_tuple))

        return tuple_struct

    def word_to_syn(self, word):
        """
        Retrieves the common synonym for a word if it exists
        :param word: Word to be checked
        :return: Common synonym if it exists
        """
        if word in self.syn_map:
            word = self.syn_map[word]

        return word

    def plag_percent(self):
        """
        Returns % plagiarism (# of common tuples)
        :return: Percent plagiarism
        """

        total_tuples = len(self.target_list)
        if total_tuples == 0:
            return 0

        plag_tuples = 0  # count of plagiarized tuples
        for tuple_ind in self.target_list:
            if tuple_ind in self.source_dict:
                plag_tuples += 1

        return (float(plag_tuples) / total_tuples) * 100

    def sanitize_word(self, word):
        """
        Converts a word to all lowercase and strips punctuation
        :param word:
        :return: sanitized word
        """
        word = word.lower()
        translator = str.maketrans('', '', string.punctuation)
        word = word.translate(translator)
        return word
