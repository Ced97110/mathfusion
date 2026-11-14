import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
text(ax, 17, 70, r'$C$ = {000, 001, 010}', 'sujet', 's')
text(ax, 71, 70, r'$001 + C$', 'autre', 's')
left = ['000', '001', '010']
right = ['000', '001', '011']
for i, (a, b) in enumerate(zip(left, right)):
    y = 54 - i * 14
    box(ax, 8, y, 18, 8, 'sujet', label=a)
    box(ax, 62, y, 18, 8, 'autre', label=b)
    if a == b:
        line(ax, [(26.5, y + 4), (61.5, y + 4)], 'limite', lw=1.2)
text(ax, 44, 50.5, 'mots communs', 'limite', 's')
text(ax, 44, 17, r'$001 + 010 = 011 \notin C$', 'limite', 's')
text(ax, 44, 8, r'$C$ n’est pas linéaire', 'limite', 's')
save(fig, '68-161')
