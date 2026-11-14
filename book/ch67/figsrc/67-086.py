import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# integers modulo 8 : 1, 3, 5, 7 squared give 1, 9, 25, 49, all equal to 1 modulo 8 (9 = 1 + 8, 25 = 1 + 24, 49 = 1 + 48)
text(ax, 44, 79, 'modulo 8 : on élève au carré', 'sujet', 'm')
X = [1, 3, 5, 7]
for k, x in enumerate(X):
    cx = 4 + k * 21
    box(ax, cx, 60, 19, 10, 'sujet', label=str(x))
    arrow(ax, (cx + 9.5, 59), (cx + 9.5, 51), 'varie')
    box(ax, cx, 41, 19, 10, 'fixe', label=str(x * x))
    arrow(ax, (cx + 9.5, 40), (cx + 9.5, 32), 'varie')
    box(ax, cx, 22, 19, 10, 'resultat', label='1')
text(ax, 44, 10, r'$(3-1)(3+1) = 8$, soit 0', 'varie', 's')
save(fig, '67-086')
