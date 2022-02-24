"""
Requests
General Information:
I want to choose random information with the requests module.
Acceptance Criteria
* Get the name, surname, city and country information of a random person by using the requests module.
(Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
* Make lowercase and adjacent by removing the spaces.
(Example=> ambermurraysalisburyunitedkingdom)
* Then randomly shuffle the location of all the characters.
(Example=> mberarrumasyarubsiluniydetmdoingk)
* Apply this process for 100 different people and write in a list.
* Find that has the most characters and print it.
"""
import requests
import random
def get_info():
    r =requests.get("https://randomuser.me/api/")
    one_info=(r.json()["results"][0]["name"]["first"],r.json()["results"][0]["name"]["last"],
    r.json()["results"][0]["location"]["city"],r.json()["results"][0]["location"]["country"])
    print(*one_info)
    one_info="".join(one_info).lower().replace(" ","")
    return one_info
mix=[]
lenght=[]
names=[]
for i in range(5):    
    mix=list(get_info())
    #print(mix)
    random.shuffle(mix)
    mix="".join(mix)
    names.append(mix)
    l=len(mix)
    lenght.append(l)
print(names)
print("\nThe Longest Text is :",max(names, key=len),"with",max(lenght),"characters\n",)
