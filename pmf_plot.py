import thinkstats2

def freqs(pmf):
    return dict((v, pmf.Prob(v)) for v in pmf.Values())

def remaining(pmf, current):
    return dict((v, pmf.Prob(v)) for v in pmf.Values() if v > current)

def remaining_lifetimes(pmf, current):
    new_pmf = thinkstats2.MakePmfFromDict(remaining(pmf, current))
    new_pmf.Normalize()
    return new_pmf

if __name__ == "__main__":
    pmf = thinkstats2.MakePmfFromList([1, 2, 2, 3, 5])
    print remaining_lifetimes(pmf, 2).__dict__