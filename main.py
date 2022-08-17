import random

hercules_stats = {
    'name' : 'Hercules',
    'health' : 100,
    'attack power' : 20,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

goblin_stats = {
    'name' : 'Goblin',
    'health' : 25,
    'attack power' : 7,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

brute_stats = {
    'name' : 'Brute',
    'health' : 120,
    'attack power' : 15,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

gnome_stats = {
    'name' : 'Gnome',
    'health' : 25,
    'attack power' : 130,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

def Get_Random(given_list):
    chosen_item = random.sample(given_list, k=1)
    return(chosen_item.pop())

def Attack(given_player, given_attacker):
    player_name = given_player.get('name')
    player_health = given_player.get('health')
    player_power = given_player.get('attack power')
    player_attack = ''
    attacker_name = given_attacker.get('name')
    attacker_health = given_attacker.get('health')
    attacker_power = given_attacker.get('attack power')
    attacker_attack = ''

    print(f'A {attacker_name} has appeard!')

    while player_health > 0 and attacker_health > 0:
        for name in given_player.get('attack names'):
            print(name)
        player_attack = input('Pick an attack!')

        attacker_health = attacker_health =- player_power
        print(f'{player_name} attacks {attacker_name} with {player_attack}!')
        print(f'{attacker_name} has {str(attacker_health)}')

        attacker_attack = Get_Random(given_attacker.get('attack names'))
        print(f'{attacker_name} attacks {player_name} with {attacker_attack}!')
        print(f'{player_name} has {str(player_health)}')


Attack(hercules_stats, goblin_stats)