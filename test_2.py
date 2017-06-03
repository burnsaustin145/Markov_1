with open('adjectives1.txt', 'r') as adj:
    adj_bank = adj.read()

with open('nounlist.txt', 'r') as noun:
    noun_bank = noun.read()


def parse(word_list):
    parsed_list = []

    for tup in word_list:
        logic_checker = ''
        for word in tup:

            if word in adj_bank:
                logic_checker += '1'
                print('1')
                print(word)
            if word in noun_bank:
                logic_checker += '0'
                print('0')
                print(word)
            else:
                pass
        if logic_checker == '10' or logic_checker == '100':
            parsed_list.append(tup)
            print(parsed_list)

        else:
            pass


    return parsed_list


print(parse([('abstract', 'web'), ('wet', 'web'), ('small', 'whale')]))
print(parse([('small', 'whale'), ('stopper_test', 'dog'), ('small', 'whale'), ('big', 'acid')]))
