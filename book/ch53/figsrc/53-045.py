import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 77, r'$ap$ : $a$ fois $p$', 'sujet', 'l', weight='bold')
for x, day, a in [(2, 'aujourd’hui', 5), (46, 'demain', 7)]:
    text(ax, x + 20, 66, day, 'fixe', 's')
    box(ax, x, 52, 40, 10, 'varie', label=f'$a$ = {a}', weight='bold')
    arrow(ax, (x + 20, 52), (x + 20, 44), 'varie')
    box(ax, x, 33, 40, 10, 'sujet', label=f'{a} fois $p$')
# les valeurs possibles de a : de 1 à 25
f = numberline(ax, 6, 76, 14, 1, 25, labels=False, arrow_right=False)
for v in (1, 25): text(ax, f(v), 14 - 4, str(v), 'fixe', 's')
for v in (5, 7):
    disc(ax, f(v), 14, 1.5, 'varie')
    text(ax, f(v), 14 - 4, str(v), 'varie', 's')
text(ax, 41, 22, '25 valeurs possibles de $a$', 'sujet', 's')
save(fig, '53-045')
