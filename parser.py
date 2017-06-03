with open('nounlist.txt', 'r') as noun:
    noun_bank = noun.read()

with open('adjectives1.txt', 'r') as adj:
    adj_bank = adj.read()


class Parser:
    """class should take pair of words, and determine if the pair is in the form adjective/noun. If so, it should
    return the pair for input to cc_markov in run.py
    """
    with open('nounlist.txt', 'r') as noun:
        noun_bank = noun.read()

    with open('adjectives1.txt', 'r') as adj:
        adj_bank = adj.read()

    def __init__(self):

        return

    def parse(self, word_list):
        parsed_list = []

        for tup in word_list:
            logic_checker = ''

            for word in tup:

                if word in adj_bank:
                    logic_checker += '1'
                if word in noun_bank:
                    logic_checker += '0'
                else:
                    pass
            if logic_checker == '10':
                parsed_list.append(tup)


            else:
                pass

        return parsed_list


    def strung_list(self, to_be_strung):
        tupstr = []
        word_pair = ''
        for tup in to_be_strung:
            for word in tup:

                word_pair += word + " "
            tupstr.append(word_pair)

            word_pair = ""



        return tupstr









