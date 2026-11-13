import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 6, 22, 36, 26, 'sujet')
for ox in (12, 56):
    for r in range(3):
        for c in range(4):
            role = 'resultat' if r == 0 else 'fixe'
            if ox == 56 and r == 2 and c == 0:
                role = 'sujet'
            disc(ax, ox + 8 * c, 43 - 8 * r, 3, role)
text(ax, 24, 56, 'unité = le paquet', 'sujet')
text(ax, 68, 56, 'unité = 1 biscuit', 'sujet')
text(ax, 24, 14, '3 biscuits = 1/4', 'resultat')
text(ax, 68, 14, '3 biscuits = 3', 'resultat')
save(fig, '06-007')
