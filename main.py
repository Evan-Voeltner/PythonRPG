import random

hercules_stats = {
    'health' : 100,
    'attack power' : 20,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

goblin_stats = {
    'health' : 25,
    'attack power' : 7,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

brute_stats = {
    'health' : 120,
    'attack power' : 15,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

gnome_stats = {
    'health' : 25,
    'attack power' : 130,
    'attack names' : ['Slash', 'Stab', 'Shove', 'Kick', 'Punch']
}

def Get_Random(given_list):
    chosen_item = random.sample(given_list, k=1)
    return(chosen_item.pop())

def Attack(given_player, given_attacker):
    player_health = given_player.get('health')
    player_power = given_player.get('attack power')
    player_attack = ''
    attacker_health = given_attacker.get('health')
    attacker_power = given_attacker.get('attack power')
    attacker_attack = Get_Random(given_attacker.get('attack names'))
    