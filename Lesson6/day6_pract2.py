import numpy as np

"""
Script for a simple game of Rock-Paper-Scissors
"""

#list of options
t = ['null','Rock', 'Paper', 'Scissors']
throws = {'r':1, 'p':2, 's':3}
win_options = {(1,3),(2,1),(3,2)}

games = int(input('To what score are we playing? '))

ai_win = 0
p_win = 0

while p_win < int(games) and ai_win < int(games):
	print(p_win, ' to ', ai_win)
	ai_hand = np.random.randint(1,4)
	p_hand = input('Rock, Paper, or Scissors? ')

	if (throws[p_hand[0].lower()], ai_hand) in win_options:
		print('Darn! Your %s beats my %s!' % (p_hand, t[ai_hand]))
		p_win +=1
	elif throws[p_hand[0].lower()] == ai_hand:
		print('Tie! We both chose %s!' % t[ai_hand])
	else:
		print('Ha! My %s beats your %s!' % (t[ai_hand], p_hand))
		ai_win +=1

print('And the winner is...')

if p_win > ai_win:
	print('You! Oh darn... Good Game!')
else:
	print("Me! Don't feel so bad... Good Game!")

