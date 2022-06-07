# To generate the "data" file in the git repo, run:
# $ git log --numstat --online > data

f = open("data", "r")

adds, dels = 0, 0
commit_hash = None
for line in f:
  #print(line)
  details = line.split()
  if len(details) < 2 or details[0] == '-': continue
  if len(details[0]) == 8:
         # commit hash or giant zip file
    if (commit_hash != None):
      cols = [commit_hash, str(adds), str(dels)]
      print(",".join(cols)) # output counts
    adds, dels = 0, 0 # reset counts
    commit_hash = details[0] 
  else:
    #print(details)
    adds += int(details[0])
    dels += int(details[1])
  
