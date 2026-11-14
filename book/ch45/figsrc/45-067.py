import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
L = ['1', '1+1', '1+1+1', '1+1+1+1']; R = ['quart', 'demi', '3 quarts', 'nulle']
text(ax, 20, 94, r'$1$ engendre', 'sujet', 'm'); text(ax, 68, 94, r'$\eta(1)$ engendre', 'resultat', 'm')
for k in range(4):
    y = 70 - k * 19
    box(ax, 4, y, 32, 11, 'sujet', label=L[k]); box(ax, 52, y, 32, 11, 'resultat', label=R[k])
    arrow(ax, (37, y + 5.5), (51, y + 5.5), 'varie')
    if k < 3:
        arrow(ax, (20, y - 0.5), (20, y - 7.5), 'fixe', lw=0.8); arrow(ax, (68, y - 0.5), (68, y - 7.5), 'fixe', lw=0.8)
text(ax, 44, 3, 'les 4 éléments sont atteints', 'resultat', 's', weight='bold')
save(fig, '45-067')
