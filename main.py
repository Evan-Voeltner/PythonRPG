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

def Attack(given_player, given_attacker):
    player_name = given_player.get('name')
    player_health = given_player.get('health')
    player_power = given_player.get('attack power')
    player_attack = ''
    attacker_name = given_attacker.get('name')
    attacker_health = given_attacker.get('health')
    attacker_power = given_attacker.get('attack power')
    attacker_attack = ''
    player_won = False

    print(f'A {attacker_name} has appeard!')

    while player_health >= 0 and attacker_health >= 0:
        for name in given_player.get('attack names'):
            print(name)
        player_attack = input('Pick an attack!: ')

        attacker_health -= player_power
        print(f'{player_name} attacks {attacker_name} with {player_attack}!')
        print(f'{attacker_name} has {str(attacker_health)}')
        if attacker_health <= 0:
            player_won = True
            break    

        attacker_attack = Get_Random(given_attacker.get('attack names'))
        player_health -= attacker_power
        print(f'{attacker_name} attacks {player_name} with {attacker_attack}!')
        print(f'{player_name} has {str(player_health)}')

    if player_won:
        return True
    else:
        return False

def RunGame(given_player, given_attackers):
    player_is_alive = True

    while player_is_alive:
        current_attacker = Get_Random(given_attackers)
        Attack(given_player, current_attacker)


RunGame(hercules_stats, attackers)
