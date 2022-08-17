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

def Attack(given_player, current_given_player_health, given_attacker):
    player_name = given_player.get('name')
    player_health = current_given_player_health
    player_power = given_player.get('attack power')
    player_attack = ''
    attacker_name = given_attacker.get('name')
    attacker_health = given_attacker.get('health')
    attacker_power = given_attacker.get('attack power')
    attacker_attack = ''
    winner_stats = {
        'name' : '',
        'health' : 0
    }

    print(f'A {attacker_name} has appeard!')

    while player_health >= 0 and attacker_health >= 0:
        for name in given_player.get('attack names'):
            print(name)
        player_attack = input('Pick an attack!: ')

        attacker_health -= player_power
        print(f'{player_name} attacks {attacker_name} with {player_attack}!')
        print(f'{attacker_name} has {str(attacker_health)} health left!')
        if attacker_health <= 0:
            winner_stats.update({'name' : player_name})
            winner_stats.update({'health' : player_health})
            break    

        attacker_attack = Get_Random(given_attacker.get('attack names'))
        player_health -= attacker_power
        print(f'{attacker_name} attacks {player_name} with {attacker_attack}!')
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
