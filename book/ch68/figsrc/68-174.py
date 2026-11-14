import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
text(ax, 44, 61, 'classe de syndrome 110', 'encre', 'm')
words = ['00110', '01011', '10101', '11000']
for k, wd in enumerate(words):
    x = 5 + k * 20
    n = wd.count('1')
    role = 'varie' if n == 2 else 'fixe'
    box(ax, x, 44, 17, 8, role, label=wd, size='s')
    text(ax, x + 8.5, 38, f'poids {n}', role, 's')
line(ax, [(13.5, 34), (13.5, 31), (73.5, 31), (73.5, 34)], 'varie')
text(ax, 44, 26, 'deux mots de poids 2', 'varie', 's')
text(ax, 44, 17, 'égalité : pas de chef unique', 'limite', 's')
text(ax, 44, 8, r'$t = 1$ : rien au-delà', 'encre', 's')
save(fig, '68-174')
