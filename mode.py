from collections import Counter

import thinkstats2

def freqs(hist):
    return [(hist.Freq(v), v) for v in hist.Values()]

def mode(hist):
    return max(freqs(hist))[1]

def sorted_freqs(hist):
    return sorted(freqs(hist), reverse=True)

if __name__ == "__main__":
    values = [1, 2, 2, 2, 3, 5]
    hist = thinkstats2.MakeHistFromList(values)
    print sorted_freqs(hist)