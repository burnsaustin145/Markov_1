class Fetch:

    def __init__(self):

        return

    def strdir(self, directory):
        text_data = ""
        for w in directory:
            with open(w, 'r') as f:
                text_data += f
        return text_data

    def strdir_2(self, text_data):
        alphabet = \
            ['a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x',
             'y', 'z'
             ]
        strtext_data = ''.lower()
        for x in text_data:
            if x in alphabet:
                strtext_data += x
            elif x == ' ':
                strtext_data += x
            else:
                pass
        return strtext_data

    def gen_pairs(self, strtext_data):
        list1 = ['offset']
        list2 = []
        split_x = strtext_data.split()

        for word in split_x:
            list1.append(word)
        for word in split_x:
            list2.append(word)
        pairs_list = zip(list1, list2)
        pairs_list = list(pairs_list)


        return pairs_list







