#ejercicios nivel 1
it_companies={'facebook','google','microsoft','apple','ibm','oracle','amazon'}
aa={19,22,24,20,25,26}
bb={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
it_companies.add('twitter')
it_companies.update(['youtube','steam','spotify','vscode'])
it_companies.remove('twitter')
print(it_companies)
print(len(it_companies))

#ejercicios nivel 2
cc=aa.union(bb)
print(cc) 
print(aa.intersection(bb))
print(aa.issubset(bb))
print(aa.isdisjoint(bb))
ab= aa.union(bb)
print(ab)
ba= bb.union(aa)
print(ba) 