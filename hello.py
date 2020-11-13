participant = {'name': 'Sarah', 'age': 3}
participant_teen = {'name': 'Britney', 'age': 11}
participant_adult = {'name': 'Chloe', 'age': 25}

def party(participant):
    print('Hello,' + participant['name'])
    if participant['age'] > 18:
        print('You can get drunk!')
    elif participant['age'] > 3:
        print('Go drink Coke!')
    else:
        print('Drink milk!')


participants = [participant, participant_teen, participant_adult]
for p in participants:
    party(p)
