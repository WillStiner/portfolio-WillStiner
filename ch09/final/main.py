from randomcat import RandomCatFactsAPI
from randomdogfacts import RandomDogFactsAPI

def determine_prefernce():
    user_preference = input("what do you prefer, cats or dogs?")
    while user_preference != "cats" and user_preference != "dogs":
        print("sorry, that won't work. you gotta give me 'cats' or 'dogs'")
        user_preference = input("what do you prefer, cats or dogs?")
    if user_preference == "cats":
        print("okay, I will give you way more cat facts")
        amount_of_cat_facts = 10
        amount_of_dog_facts = 1
    elif user_preference == "dogs":
        print("okay, I will give you way more dog facts")
        amount_of_cat_facts = 1
        amount_of_dog_facts = 10
    return amount_of_cat_facts, amount_of_dog_facts

def main():
    amount_of_cat_facts, amount_of_dog_facts = determine_prefernce()
    cat_api = RandomCatFactsAPI(amount_of_cat_facts)
    dog_api = RandomDogFactsAPI(amount_of_dog_facts)
    cat_api.get()
    dog_api.get()


main()