def filter_by_legth(words):
    return[word for word in words if len(word) > 3]

words = ['amor', 'sol', 'piedra', 'dia']
response = filter_by_legth(words)
print(response)