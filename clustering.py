def cluster(values, threshold):
    return [int(value >= threshold) for value in values]
