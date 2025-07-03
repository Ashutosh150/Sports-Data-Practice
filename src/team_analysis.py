import random

def create_team():
    team = []
    n = int(input('No of player: '))
    for i in range(n):
        name = input(f'Enter player{i} detail: ')
        position = random.randint(0, 100)
        jersey_number = random.randint(0, 11)
        player = {
            'name': name,
            'position': position,
            'jersey_number': jersey_number
        }
        team.append(player)
    return team

def print_positions(team):
    position_list = [i['position'] for i in team]
    print('Player positions:', position_list)

def update_player_stats(team):
    team_stat_update = input('Enter player name to add stats: ')
    found = False
    for i in team:
        if i['name'] == team_stat_update:
            i['yards gained'] = random.randint(1, 50)
            i['touchdowns'] = random.randint(1, 50)
            found = True
            break
    if not found:
        print('Player not found')

def calculate_averages(team):
    total_yards = 0
    total_touchdowns = 0
    count_yards = 0
    count_touchdowns = 0
    for i in team:
        if 'yards gained' in i:
            total_yards += i['yards gained']
            count_yards += 1
        if 'touchdowns' in i:
            total_touchdowns += i['touchdowns']
            count_touchdowns += 1
    avgY = total_yards / count_yards if count_yards > 0 else 0
    avgT = total_touchdowns / count_touchdowns if count_touchdowns > 0 else 0
    print('Average yards gained:', avgY)
    print('Average touchdowns:', avgT)

def main():
    team = create_team()
    print_positions(team)
    update_player_stats(team)
    calculate_averages(team)

if __name__ == "__main__":
    main()
