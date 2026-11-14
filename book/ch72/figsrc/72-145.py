import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
text(ax, 44, 67, 'rotation de l’espace', 'sujet', 'l', weight='bold')
text(ax, 44, 60, 'à 3 dimensions', 'sujet', 'l', weight='bold')
f = lambda k: 14 + k * 20
brace(ax, f(0) - 5, f(3) + 5, 45, 'sujet', down=False, label='au plus 3 réflexions')
for k in range(4):
    ok = k % 2 == 0
    role = 'resultat' if ok else 'limite'
    disc(ax, f(k), 36, 4.6, role, label=str(k), size='l')
    text(ax, f(k), 26, 'pair' if ok else 'impair', role, 's')
text(ax, 44, 19, r'$k$ = nombre de réflexions', 'encre', 's')
box(ax, 8, 2, 72, 10, 'resultat', label='rotation : 0 ou 2 réflexions', size='m', weight='bold')
save(fig, '72-145')
