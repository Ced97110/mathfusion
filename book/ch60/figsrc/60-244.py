import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 3, 64, r'$n=30$', 'sujet', 'l', ha='left')
for i, p in enumerate((2, 3, 5)):
    box(ax, 3 + 12 * i, 48, 9, 9, 'sujet', label=str(p))
text(ax, 65, 55, 'aucun premier répété', 'fixe', 's')
text(ax, 65, 49, '1 groupe', 'resultat', 'l')
line(ax, [(3, 38), (85, 38)], 'fixe', lw=0.5, dash=True)
text(ax, 3, 32, r'$n=32$', 'sujet', 'l', ha='left')
for i in range(5):
    box(ax, 3 + 12 * i, 16, 9, 9, 'varie', label='2')
text(ax, 74, 23, 'premier répété', 'varie', 's')
text(ax, 74, 17, '7 groupes', 'resultat', 'l')
save(fig, '60-244')
