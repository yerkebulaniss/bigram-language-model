import pandas as pd


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


def visualize_probabilities(probabilities):
    df = pd.DataFrame.from_dict(probabilities, orient='index', columns=['Probability'])
    df = df.sort_index()
    print(df)


def main():
    names = read_names('names.txt')
    bigram_model = build_bigram_model(names)
    probabilities = calculate_probabilities(bigram_model)
    visualize_probabilities(probabilities)


if __name__ == '__main__':
    main()
