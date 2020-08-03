# replace char at a given position with another char
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
