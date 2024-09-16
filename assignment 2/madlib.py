def madlib(adverb_1, noun_1, verb_1,adverb_2, noun_2, verb_2,adverb_3, noun_3, verb_3, noun_4):
    story = f'''
One day, a {noun_1} decided to {verb_1} through the {noun_2}. 
It moved very {adverb_1}, hoping not to {verb_2} anyone's attention.
Suddenly, it stumbled upon a {noun_3} that was {adverb_2} waiting for something exciting to happen.
Without thinking, the {noun_4} quickly decided to {verb_3}, and everything changed forever!
'''
    return story


def get_user_input():
    adverb_1 = input("Enter adv: ")
    noun_1 = input("Enter noun: ")
    verb_1 = input("Enter verb: ")
    adverb_2 = input("Enter adv: ")
    noun_2 = input("Enter noun: ")
    verb_2 = input("Enter verb: ")
    adverb_3 = input("Enter adv: ")
    noun_3 = input("Enter noun: ")
    verb_3 = input("Enter verb: ")
    noun_4 = input("Enter noun: ")
    return adverb_1, noun_1, verb_1,adverb_2, noun_2, verb_2,adverb_3, noun_3, verb_3, noun_4

users_input = get_user_input()
output_story = madlib('slowly', 'dog', 'do', 'quickly', 'cat', 'run', 'gently', 'profs', 'eat', 'bottle')
print(output_story)
