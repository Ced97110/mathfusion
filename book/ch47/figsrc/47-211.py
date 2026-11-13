import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 30, 62, '8 symétries en 4 classes de 2', 'encre', 's')
labs = ['A', 'B', 'C', 'D']
for k in range(4):
    y = 46 - k*12
    r = 'sujet' if k == 0 else 'fixe'
    box(ax, 6, y - 4, 7, 8, r); box(ax, 15, y - 4, 7, 8, r)
    arrow(ax, (24, y), (47, y), 'varie' if k == 0 else 'fixe')
    disc(ax, 54, y, 4.5, 'varie' if k == 0 else 'fixe', label=labs[k], size='m')
text(ax, 54, 57, 'orbite : 4 sommets', 'varie', 's', ha='center')
text(ax, 77, 46, r'$H$ =', 'sujet', 's'); text(ax, 77, 41, 'laisse A', 'sujet', 's')
text(ax, 44, 3, r'$8\div2=4$', 'resultat', 'm', weight='bold')
save(fig, '47-211')
