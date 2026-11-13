import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
for b, cx in enumerate([16, 44, 72]):
    text(ax, cx, 68, f'image de {b + 1}', 'sujet', 's')
    for k in range(3):
        tx = cx - 9 + 9 * k
        disc(ax, tx, 46, 3.6, 'varie', label=str(k + 1), size='s'); arrow(ax, (cx, 65.5), (tx, 50), 'sujet', lw=0.7)
text(ax, 44, 28, r'$3 \times 3 \times 3 = 27$', 'resultat', 'l', weight='bold')
text(ax, 44, 14, r'pour $n$ éléments : $n^{n}$', 'sujet', 'm')
save(fig, '44-046')
