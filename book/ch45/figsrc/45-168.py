import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 55, 49, 'cadran (ℤ/3)', 'autre'); text(ax, 12, 32, 'interrupteur\n(ℤ/2)', 'sujet')
for a in range(2):
    for b in range(3): box(ax, 25 + 20 * b - 0, 36 - 14 * a - 10 + 10 - 10 + 0 if False else 27 - 14 * a, 18, 10, 'sujet', label=f'({a}, {b})')
text(ax, 55, 6, r'$2\times3=6$ états', 'resultat')
save(fig, '45-168')
