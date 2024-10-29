from perplexity import Perplexity

perplexity = Perplexity("irontmp+ks8ra@gmail.com")


answer = perplexity.search("Who won the ballondor this year.")
for a in answer:
    if a.get('status')=='completed':
        print(a)
perplexity.close()