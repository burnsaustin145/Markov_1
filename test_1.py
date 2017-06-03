from fetch_data import Fetch
from parser import Parser

with open('/Users/macbook/PycharmProjects/markov_1/txt_data/4-24: goals copy.txt') as test_file:
    read_file = test_file.read()

f = Fetch()
p = Parser()

str_text = f.strdir_2(read_file)
print("strdir_2")
print(str_text)
txt_markov = f.gen_pairs(str_text)
print("gen_paris")
print(txt_markov)
parsed = p.parse(txt_markov)
print("parsed")
print(parsed)

