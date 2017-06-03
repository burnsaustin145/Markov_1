"""Things I would still like to do:
improve accuracy of parser
add feature for inputting multiple text files easily
add formatting to output, as well as statistics"""

from fetch_data import Fetch
from markov_python.cc_markov import MarkovChain
from parser import Parser

with open('nounlist.txt', 'r') as noun:
    noun_bank = noun.read()

with open('adjectives1.txt', 'r') as adj:
    adj_bank = adj.read()

##user must enter their own text file here
with open('/Users/macbook/PycharmProjects/markov_1/txt_data/4-24: goals copy.txt') as test_file:
    read_file = test_file.read()

fetch = Fetch()
mc = MarkovChain()
p = Parser()


def adder(string_tobe_strung):
    mf_string = ''
    for pair in string_tobe_strung:
        mf_string += pair + ", "

    return mf_string

##prints at each function the text goes through
str_text = fetch.strdir_2(read_file)
print("str_text")
print(str_text)

txt_markov = fetch.gen_pairs(str_text)
print("txt_markov")
print(txt_markov)

parsed_markov = p.parse(txt_markov)
print("parsed_markov")
print(parsed_markov)

strung = p.strung_list(parsed_markov)
print("strung text")
print(strung)

mf_final_string = adder(strung)
mc.add_string(mf_final_string)
print("final string to be feed into markov chain")
print(mf_final_string)

print("final_text")
final_text = mc.generate_text(25)
print(final_text)

print("lookup dictionary")
print(mc.lookup_dict)













