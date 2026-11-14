import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# corps à 8 éléments sur le corps à 2 éléments (k = 3) : combien d'éléments vérifient chaque égalité ?
cw, x0 = 5.2, 22
text(ax, 44, 82, '8 éléments du grand corps', 'fixe', 's')
rows = [(r'$\alpha^2 = \alpha$', 2, 'au plus 2'), (r'$\alpha^4 = \alpha$', 4, 'au plus 4'), (r'$\alpha^8 = \alpha$', 8, 'les 8')]
ys = [66, 46, 26]
for (lab, n, note), y in zip(rows, ys):
    text(ax, 2, y + 4, lab, 'encre', 's', ha='left')
    for i in range(8):
        if i < n:
            box(ax, x0 + i * cw, y, cw, 8, 'resultat' if n == 8 else 'sujet', lw=0.6, r=0.2)
        else:
            box(ax, x0 + i * cw, y, cw, 8, 'limite', lw=0.6, r=0.2, dash=True)
    text(ax, x0 + 8 * cw + 2, y + 4, note, 'resultat' if n == 8 else 'sujet', 's', ha='left')
text(ax, 44, 59, 'certains éléments échappent', 'limite', 's')
text(ax, 44, 39, 'certains éléments échappent', 'limite', 's')
text(ax, 44, 14, r'$\alpha \mapsto \alpha^2$ : ordre exactement 3', 'resultat', 'm')
text(ax, 44, 6, r'1 application : non ; 2 : non ; 3 : oui', 'resultat', 's')
save(fig, '63-191')
