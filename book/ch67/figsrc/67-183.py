import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'doubler l’exposant (mod 15)', 'encre', 'm')
rows = [([1, 2, 4, 8], 'sujet'), ([3, 6, 12, 9], 'sujet'), ([7, 14, 13, 11], 'sujet'), ([5, 10], 'autre'), ([0], 'resultat')]
for i, (ex, role) in enumerate(rows):
    y = 62 - 11 * i
    box(ax, 3, y - 4, 52, 8, role, label=' → '.join(map(str, ex)), size='m')
    for j in range(len(ex)):
        disc(ax, 64 + 6 * j, y, 2.2, role)
text(ax, 44, 8, '4 + 4 + 4 + 2 + 1 = 15 éléments', 'resultat', 'm')
save(fig, '67-183')
