import thinkstats2 as stats
from births import first_births, other_births, live_births

def probs(pmf):
    return [(pmf.Prob(v), v) for v in pmf.Values()]

def preg_lengths(records):
    return [r.prglength for r in records]

def ProbEarly(pmf):
    # Week 37 or earlier
    probabilities = probs(pmf)
    return sum([x[0] for x in probabilities if x[1] <= 37])

def ProbOnTime(pmf):
    # Week 38 - 40
    probabilities = probs(pmf)
    return sum([x[0] for x in probabilities if 38 <= x[1] <= 40])

def ProbLate(pmf):
    # Weeks 41 +
    probabilities = probs(pmf)
    return sum([x[0] for x in probabilities if x[1] >= 41])

def Timing(pmf):
    return ProbEarly(pmf), ProbOnTime(pmf), ProbLate(pmf)

def Ratio(pmf1, pmf2):
    timing1 = Timing(pmf1)
    timing2 = Timing(pmf2)
    return [timing1[i]/timing2[i] for i in range(len(timing1))]


if __name__ == "__main__":
    pmf_live_births = stats.MakePmfFromList(preg_lengths(live_births))
    pmf_first_births = stats.MakePmfFromList(preg_lengths(first_births))
    pmf_other_births = stats.MakePmfFromList(preg_lengths(other_births))
    print Timing(pmf_live_births)
    print Timing(pmf_first_births)
    print Ratio(pmf_first_births, pmf_live_births)
