import survey
table = survey.Pregnancies()
table.ReadRecords()
live_births  =  [r for r in table.records if r.outcome == 1]
first_births = [r for r in live_births if r.birthord == 1]
other_births = [r for r in live_births if r.birthord != 1]