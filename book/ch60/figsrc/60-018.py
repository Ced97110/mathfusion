import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cw, ch, x0, yt = 11, 9, 12, 58
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
spec = {(2, 2): ('sujet', '2'), (2, 1): ('autre', '10')}
for i in range(4):
    for j in range(3):
        role, lab = spec.get((i, j), ('resultat', None))
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, role, label=lab, size='m', r=0.6)
for i in range(4): text(ax, x0 - 3, ctr(i, 0)[1], str(i), 'fixe', 's')
for j in range(3): text(ax, ctr(0, j)[0], yt + 3, str(j), 'fixe', 's')
text(ax, 44, 72, '12 nombres, 12 cases : aucune vide', 'resultat', 'm')
text(ax, x0 + 1.5 * cw, yt + 8, 'reste mod 3 (colonne)', 'fixe', 's')
text(ax, 2.5, yt - 2 * ch, 'reste mod 4 (ligne)', 'fixe', 's', rot=90)
text(ax, 52, 40, '10 − 2 = 8 = 2 × 4 :\nmême ligne 2', 'encre', 's', ha='left')
text(ax, 52, 26, '8 n’est pas multiple de 3 :\ncolonnes 2 et 1', 'encre', 's', ha='left')
save(fig, '60-018')
