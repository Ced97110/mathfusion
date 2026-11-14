import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(104)
steps = [(88, 'sujet', 'départ : $H$ non vide, $g - h \\in H$'), (70, 'fixe', '$h = g$ donne le neutre $e$'), (54, 'fixe', '$g = e$ donne l’inverse de $h$'), (38, 'varie', '$g - h^{-1}$ donne le produit'), (14, 'resultat', 'neutre, inverse, produit dans $H$')]
for y, role, t in steps:
    h = 12 if y in (88, 14) else 10
    box(ax, 4, y, 64, h, role, label=t, size='s', lw=1.2 if role == 'varie' else 0.8)
for (y1, _, _), (y2, _, _) in zip(steps[:-1], steps[1:]):
    top = y1; bottom = y2 + (12 if y2 == 14 else 10)
    arrow(ax, (36, top), (36, bottom), 'fixe')
text(ax, 78, 43, 'étape\ndécisive', 'varie', 's')
save(fig, '46-048')
