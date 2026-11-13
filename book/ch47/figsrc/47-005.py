import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [12, 40, 68]
text(ax, 44, 64, 'Horloge à 12 heures', 'encre', 'm')
for x, t, r in zip(xs, ['26', '27', '53'], ['sujet', 'sujet', 'sujet']):
    box(ax, x - 8, 44, 16, 10, r, label=t, size='l')
for x, t, r in zip(xs, ['2', '3', '5'], ['varie', 'varie', 'resultat']):
    box(ax, x - 8, 6, 16, 10, r, label=t, size='l')
for x in (26, 54):
    text(ax, x, 49, '+' if x == 26 else '=', 'encre', 'l')
    text(ax, x, 11, '+' if x == 26 else '=', 'encre', 'l')
for x in xs:
    arrow(ax, (x, 42), (x, 18), 'varie')
    text(ax, x + 9, 30, 'reste', 'varie', 's')
save(fig, '47-005')
