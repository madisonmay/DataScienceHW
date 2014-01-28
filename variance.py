import thinkstats2 as stats
from math import sqrt

from risk import pmf_live_births, pmf_first_births, pmf_other_births

def mean(pmf):
    return sum([pmf.Prob(v)*v for v in pmf.Values()])

def variance(pmf):
    average = mean(pmf)
    return sum([pmf.Prob(v)*(v-average)**2 for v in pmf.Values()])

def std_dev(pmf):
    return sqrt(variance(pmf))

if __name__ == "__main__":
    print mean(pmf_first_births), mean(pmf_other_births)
    print std_dev(pmf_first_births), std_dev(pmf_other_births)


"""
What we've learned:

Basic summary statistics like the mean of a distribution provide a very 
limited picture -- we really need to see a histogram or have std-deviations
listed in order to get a more complete picture.  

First babies are in fact more likely to arrive late (about 25% more likely)
and are also more likely to arrive early.  This is a nuance we wouldn't have 
picked up if we hadn't broken the dataset down into groups.

Summary stats for evening news:
--First borns 25% more likely to be born late

Summary stats for anxious patient
--More likely for first borns not to be on time (nothing to worry about)
--Rough explanation of std-deviation + explain that it's not unusual for 
kids to be 2-3 weeks late.


"""