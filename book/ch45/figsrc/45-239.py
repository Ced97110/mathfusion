import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$\mathrm{ordre}(a)=n\,/\,\mathrm{PGCD}(a,n)$', 'sujet', 'l', weight='bold')
text(ax, 44, 66, r'dans $\mathbb{Z}/12$ : $n=12$', 'encre', 's')
def row(y, head, vis, role):
    text(ax, 4, y + 9, head, role, 'm', ha='left', weight='bold')
    for k in range(12):
        box(ax, 4 + k * 6.9, y, 6.4, 6.4, role if k in vis else 'fixe', fill=True, r=0.4, lw=0.6 if k in vis else 0.4)
    text(ax, 4 + 3.2, y - 3, '0', 'fixe', 's'); text(ax, 4 + 11 * 6.9 + 3.2, y - 3, '11', 'fixe', 's')
row(44, r'$a=5$ : PGCD 1, ordre 12', range(12), 'resultat')
row(20, r'$a=8$ : PGCD 4, ordre 3', [0, 4, 8], 'varie')
text(ax, 44, 8, 'cases visitées avant retour à 0', 'fixe', 's')
save(fig, '45-239')
