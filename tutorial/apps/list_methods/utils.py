

def start_game(data):
    for pl, sc in zip(data['players'], data['scores']):
        print("Player :  %s     Score : %d" % (pl, sc))
