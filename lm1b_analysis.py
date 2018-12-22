occurrences = {
    'ie': 0,
    'ei': 0,
    'cie': 0,
    'cei': 0,

    'ie_count': 0,
    'ei_count': 0,
    'cie_count': 0,
    'cei_count': 0,

    'cie_words': [],
    'cei_words':  []

}

with open("1b_word_vocab.txt") as fd:
    i = 0
    for line in fd:
        i += 1
        word, count = line.split(" ")
        count = int(count)
        word = word.lower()

        if i % 500:
            print(i)

        if 'ie' in word:
            occurrences['ie'] += count
            occurrences['ie_count'] += 1

            if 'cie' in word:
                occurrences['cie'] += count
                occurrences['cie_count'] += 1
                occurrences['cie_words'].append(word)

        if 'ei' in word:
            occurrences['ei'] += count
            occurrences['ei_count'] += 1

            if 'cei' in word:
                occurrences['cei'] += count
                occurrences['cei_count'] += 1
                occurrences['cei_words'].append(word)


print("========== WEIGHTED RESULTS ==========")
total = occurrences['ie'] + occurrences['ei']
print("ie % = {}".format(occurrences['ie'] / total))
print("ei % = {}".format(occurrences['ei'] / total))

c_total = occurrences['cie'] + occurrences['cei']
print("cei % = {}".format(occurrences['cei'] / c_total))
print("cie % = {}".format(occurrences['cie'] / c_total))

print("========== NON-WEIGHTED RESULTS ==========")
total = occurrences['ie_count'] + occurrences['ei_count']
print("ie % = {}".format(occurrences['ie_count'] / total))
print("ei % = {}".format(occurrences['ei_count'] / total))

c_total = occurrences['cie_count'] + occurrences['cei_count']
print("cei % = {}".format(occurrences['cei_count'] / c_total))
print("cie % = {}".format(occurrences['cie_count'] / c_total))


# Save examples to disk
with open("cei_words.txt", 'w') as f:
    for word in occurrences['cei_words']:
        f.write(word + "\n")

with open("cie_word.txt", 'w') as f:
    for word in occurrences['cie_words']:
        f.write(word + "\n")




