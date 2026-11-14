import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$e_2=x_1x_2+x_1x_3+x_2x_3$', 'sujet', 'l')
cols = [48, 61, 74]
w, h = 11, 10
for i, x in enumerate(cols):
    text(ax, x + w / 2, 58, rf'$x_{i + 1}$', 'fixe', 'm')
rows = [(r'$x_1x_2$', (1, 1, 0), 40), (r'$x_1x_3$', (1, 0, 1), 26), (r'$x_2x_3$', (0, 1, 1), 12)]
for lab, ex, y in rows:
    text(ax, 40, y + h / 2, lab, 'sujet', 'm', ha='right')
    for x, k in zip(cols, ex):
        if k:
            box(ax, x, y, w, h, 'sujet')
        else:
            box(ax, x, y, w, h, 'fixe', fill=False, dash=True)
box(ax, 2, 38.5, 82, 13, 'resultat', fill=False, lw=1.4, r=1.5)
text(ax, 4, 58, 'le plus haut', 'resultat', 'm', ha='left', weight='bold')
text(ax, 44, 4, 'plein : exposant 1 ; vide : 0', 'fixe', 's')
save(fig, '55-097')
