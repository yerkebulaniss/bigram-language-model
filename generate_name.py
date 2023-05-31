import random


def read_names(filename):
    with open(filename, 'r') as file:
        names = file.read().splitlines()
    return names


def build_bigram_model(names):
    bigram_model = {}
    for name in names:
        name = '^' + name + '$'
        for i in range(len(name) - 1):
            bigram = name[i:i+2]
            if bigram not in bigram_model:
                bigram_model[bigram] = 1
            else:
                bigram_model[bigram] += 1
    return bigram_model


def calculate_probabilities(bigram_model):
    total_count = sum(bigram_model.values())
    probabilities = {}
    for bigram, count in bigram_model.items():
        probabilities[bigram] = count / total_count
    return probabilities


def generate_name(probabilities):
    name = ''
    bigram = random.choice(list(probabilities.keys()))
    while bigram[1] != '$':
        name += bigram[1]
        next_bigram = get_next_bigram(bigram, probabilities)
        bigram = next_bigram
    return name


def get_next_bigram(bigram, probabilities):
    possible_bigrams = [next_bigram for next_bigram in probabilities.keys() if next_bigram.startswith(bigram[1])]
    if len(possible_bigrams) == 0:
        next_bigram = random.choice(list(probabilities.keys()))
    else:
        probabilities_list = [probabilities[next_bigram] for next_bigram in possible_bigrams]
        next_bigram = random.choices(possible_bigrams, probabilities_list)[0]
    return next_bigram


def main():
    names = read_names('names.txt')
    bigram_model = build_bigram_model(names)
    probabilities = calculate_probabilities(bigram_model)
    name = generate_name(probabilities)
    print("Generated Name:", name)


if __name__ == '__main__':
    main()
