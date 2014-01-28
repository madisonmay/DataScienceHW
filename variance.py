import thinkstats2 as stats
from math import sqrt

def mean(pmf):
    return sum([pmf.Prob(v)*v for v in pmf.Values()])

def variance(pmf):
    average = mean(pmf)
    return sum([pmf.Prob(v)*(v-average)**2 for v in pmf.Values()])

if __name__ == "__main__":
    lst = [4, 6]
    pmf = stats.MakePmfFromList(lst)
    print mean(pmf)
    print variance(pmf)