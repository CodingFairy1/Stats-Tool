
import constants
import copy


players_copy = copy.deepcopy(constants.PLAYERS)


def clean_data():
    int_height()
    bool_exp()

def int_height():
    for player in players_copy:
        player_inches = player['height'].split(' ')
        player_height_num = int(player_inches[0])
        player['height'] = player_height_num 
        
def bool_exp():
    for player in players_copy:
        experience_test = player['experience']
        if experience_test == 'YES':
            player['experience'] = True
        elif experience_test == 'NO':
            player['experience'] = False

def balance_teams():
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    # The answer equals 6^
    panthers = []
    bandits = []
    warriors = []
    all_teams = [panthers, bandits, warriors]
    num_teams = len(all_teams)
    for num in range(len(players_copy)):
        all_teams[num % num_teams].append(players_copy[num])
    return (panthers, bandits, warriors)

def menu():
    print('(>^3^)>o * ~BASKETBALL TEAM STATS TOOL~ * o<(^u^<)')
    print('\n--- MENU ---')
    print('\nHere are your choices:\n\n 1) View Team Stats\n 2) Exit Program')
    choice = input('\nEnter your option > ')
    if choice == '1':
        print('\n 1) Panthers\n 2) Bandits\n 3) Warriors')
        team_select = input('\nEnter your option > ')
        if team_select == '1':
            panther_list = balance_teams()[0]
            player_amount = len(panther_list)
            print('\nTeam: Panthers\n~*~*~*~*~*~*~*~*\nPlayers: {}\n'.format(player_amount))
            names_list1 = []
            for player in panther_list:
                player_names = player['name']
                names_list1.append(str(player_names))
            print(", ".join(names_list1))
        elif team_select == '2':
            bandit_list = balance_teams()[1]
            player_amount = len(bandit_list)
            print('\nTeam: Bandits\n~*~*~*~*~*~*~*~*\nPlayers: {}\n'.format(player_amount))
            names_list2 = []
            for player in bandit_list:
                player_names = player['name']
                names_list2.append(str(player_names))
            print(", ".join(names_list2))
        elif team_select == '3':
            warrior_list = balance_teams()[2]
            player_amount = len(warrior_list)
            print('\nTeam: Bandits\n~*~*~*~*~*~*~*~*\nPlayers: {}\n'.format(player_amount))
            names_list3 = []
            for player in warrior_list:
                player_names = player['name']
                names_list3.append(str(player_names))
            print(", ".join(names_list3))
    elif choice == '2':
        while True:
            break
    
    

if __name__ == '__main__':
    clean_data()
    balance_teams()
    menu()
