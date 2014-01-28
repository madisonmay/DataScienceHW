import survey
table = survey.Pregnancies()
table.ReadRecords()
live_births  =  [r for r in table.records if r.outcome == 1]
first_births = [r for r in live_births if r.birthord == 1]
other_births = [r for r in live_births if r.birthord != 1]
average = lambda l: sum(l)/float(len(l))

average_fb_pregnancy_length = average([r.prglength for r in first_births])
average_other_pregnancy_length = average([r.prglength for r in other_births])

print "Number of Pregnancies:", len(table.records)
print "Live Births:", len(live_births)
print "First Born Live Births:", len(first_births)
print "Other Live Births:", len(other_births)
print "Average Pregnancy Length - First Born:", average_fb_pregnancy_length, "weeks"
print "Average Pregnancy Length - Other:", average_other_pregnancy_length, "weeks"
