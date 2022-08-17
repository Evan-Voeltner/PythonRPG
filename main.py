import random

hercules_stats = {
    'name' : 'Hercules',
    'health' : 100,
    'attack power' : 20,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

attackers = [
    {
    'name' : 'Goblin',
    'health' : 25,
    'attack power' : 7,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']},
    {
    'name' : 'Brute',
    'health' : 120,
    'attack power' : 15,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']},
    {
    'name' : 'Gnome',
    'health' : 25,
    'attack power' : 130,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']}
    ]

def Get_Random(given_list):
    chosen_item = random.sample(given_list, k=1)
    return(chosen_item.pop())

def VerifyChoice(given_choice, given_choices_list):
    response_is_valid = False
    current_response = given_choice
    while response_is_valid != True:
        for option in given_choices_list:
            if option == current_response.capitalize():
                response_is_valid = True
        
        if response_is_valid != True:
            current_response = input('Please type a valid response: ')

    return(current_response)        

def HowMuchDamage(starting_health, damage_delt):
    precentage_of_health = damage_delt/starting_health

    if precentage_of_health <= .25:
        return('small')
    if precentage_of_health >= .26 and precentage_of_health <= .50:
        return('medium')
    if precentage_of_health >= .51:
        return('large')

def HowMuchHealth(starting_health, health_left):
    precentage_of_health = health_left/starting_health

    if precentage_of_health <= .50:
        return('small')
    else:
        return('large')

def RecipientResponse(starting_health, damage_delt, health_left, type_of_attack):
    amount_of_damage_delt_responses = {
        'small' : ['Hahaha! ', '*yawn. ', 'Ehh... nice try. '],
        'medium' : ['Gah! ','Ow! ','Jeez! '],
        'large' : ['AHHH!!!!!! ','F***!!! ','WHY! OMG! WHY! OW! OW! OW! ']    
        }
    type_of_attack_responses = {
        'slash' : ['That was quite the slash, ', 'Your sword lays an adequate blow, ', 'Your swing was heavy and courageous, '],
        'stab' : ['That was quite the stab, ','An impalement all the rest, ','I see you have made a hole out of me, '],
        'shove' : ['That was quite the shove, ','Discombobulation never seems to get old, ','Too good for a punch I see, '],
        'kick' : ['That was quite the kick, ', 'It appears your legs lacked attention, ', 'I see you like to play footsie, '],
        'punch' : ['That was quite the punch, ','I guess I never heard the bell ring, ','That one is quite the fan favorite, ']      
    }
    amount_of_health_left_responses = {
        'small' : ['I am holding on by a mere thread.','it appears that my days are numbered.','my presence as a matter of conceren, is to be no more.'],
        'large' : ['I still seem to be holding on.', 'like an unrattled leaf, I remain present.', 'yet the sun still shines another day']
    }

    amount_of_damage = HowMuchDamage(starting_health, damage_delt)
    amount_of_health = HowMuchHealth(starting_health, health_left)

    first_segment = Get_Random(amount_of_damage_delt_responses.get(amount_of_damage))
    middle_segment = Get_Random(type_of_attack_responses.get(type_of_attack.lower()))
    last_segment = Get_Random(amount_of_health_left_responses.get(amount_of_health))
    
    and_or_but = ''

    if amount_of_damage == 'small' and amount_of_health == 'small':
        and_or_but = 'but '
    if amount_of_damage == 'medium' or amount_of_damage == 'large' and amount_of_health == 'large':
        and_or_but = 'but '
    else:
        and_or_but = 'and '

    print(f'{first_segment}{middle_segment}{and_or_but}{last_segment}')

def Attack(given_player, current_given_player_health, given_attacker):
    player_name = given_player.get('name')
    player_health = current_given_player_health
    player_starting_health = current_given_player_health
    player_power = given_player.get('attack power')
    player_attack_names = given_player.get('attack names')
    player_attack = ''
    attacker_name = given_attacker.get('name')
    attacker_health = given_attacker.get('health')
    attacker_starting_health = given_attacker.get('health')
    attacker_power = given_attacker.get('attack power')
    attacker_attack = ''
    winner_stats = {
        'name' : '',
        'health' : 0
    }

    print(f'A {attacker_name} has appeard!')

    while player_health >= 0 and attacker_health >= 0:
        for name in player_attack_names:
            print(name)
        player_attack = VerifyChoice(input('Pick an attack!: '), player_attack_names) 

        attacker_health -= player_power

        print(f'{player_name} attacks {attacker_name} with {player_attack}!')
        RecipientResponse(attacker_starting_health, player_power, attacker_health, player_attack)
        print(f'{attacker_name} has {str(attacker_health)} health left!')
        
        if attacker_health <= 0:
            winner_stats.update({'name' : player_name})
            winner_stats.update({'health' : player_health})
            break    

        attacker_attack = Get_Random(given_attacker.get('attack names'))
        player_health -= attacker_power

        print(f'{attacker_name} attacks {player_name} with {attacker_attack}!')
        RecipientResponse(player_starting_health, attacker_power, player_health, attacker_attack)
        print(f'{player_name} has {str(player_health)} health left!')
        
        if player_health <= 0:
            winner_stats.update({'name' : attacker_name})
            winner_stats.update({'health' : attacker_health})
            break 

    return(winner_stats)

def RunGame(given_player, given_attackers):
    player_is_alive = True
    player_name = given_player.get('name')
    player_health = given_player.get('health')

    while player_is_alive:
        current_attacker = Get_Random(given_attackers)
        attacker_name = current_attacker.get('name')
        attack_result = Attack(given_player, player_health, current_attacker)
        
        if attack_result.get('name') == player_name:
            player_health = attack_result.get('health')
            print(f'{player_name} beat {attacker_name}! {player_name} has {str(player_health)} health left.')
        else:
            attacker_health = str(attack_result.get('health'))
            print(f'{player_name} lost their battle with {attacker_name}! {attacker_name} beat them out with {attacker_health} health left.')  
            player_is_alive = False


RunGame(hercules_stats, attackers)
