import re


def convert(x):
    x = int(x)
    if 90 <= x <= 100:
        return 4.0
    elif 85 <= x <= 89:
        return 3.7
    elif 82 <= x <= 84:
        return 3.3
    elif 78 <= x <= 81:
        return 3.0
    elif 75 <= x <= 77:
        return 2.7
    elif 72 <= x <= 74:
        return 2.3
    elif 68 <= x <= 71:
        return 2.0
    elif 64 <= x <= 67:
        return 1.5
    elif 60 <= x <= 63:
        return 1.0
    else:
        return 0.0


if __name__ == '__main__':

    f = open('score.html')
    content = f.readlines()
    f.close()

    interest = filter(lambda x: x.strip().startswith("<td align='left'>"), content)
    weights = interest[7::13]
    scores = interest[9::13]

    weights = map(lambda x: float(re.findall(r'\d+', x)[0]), weights)
    scores = map(lambda x: convert(re.findall(r'\d+', x)[0]), scores)

    total = 0.0
    for i in range(len(weights)):
        total += weights[i] * scores[i]

    print 'score = %.3f' % (total / sum(weights))

