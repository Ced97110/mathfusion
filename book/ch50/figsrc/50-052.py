import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X0, CW, CH = 8.0, 9.0, 7.0
def cell(i, y, role, fill=True, dash=False, label=None):
    box(ax, X0 + i * CW, y, CW - 0.8, CH, role, fill=fill, dash=dash, r=0.5, lw=0.7, label=label, size='s')
# rangée 1 : S3 a 6 éléments, le sous-groupe en compte 2
text(ax, 44, 72, r'$S_3$ : 6 éléments', 'sujet', 's')
for i in range(6):
    if i == 0: cell(i, 60, 'sujet', label='$e$')
    elif i == 1: cell(i, 60, 'sujet', label='$s_A$')
    else: cell(i, 60, 'fixe')
# rangée 2 : paquet de 4 dans 6
text(ax, 44, 50, 'taille 4 : il reste 2', 'varie', 's')
for i in range(6):
    cell(i, 38, 'varie' if i < 4 else 'limite')
# rangée 3 : paquet de 8 dans 6
text(ax, 44, 28, 'taille 8 : il manque 2', 'varie', 's')
for i in range(8):
    if i < 6: cell(i, 16, 'varie')
    else: cell(i, 16, 'limite', fill=False, dash=True)
text(ax, 44, 6, 'aucun sous-groupe plus grand : maximal', 'resultat', 's')
save(fig, '50-052')
