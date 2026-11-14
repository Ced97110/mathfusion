import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 80, 'T² + 1 = 0', 'sujet', 'xl', weight='bold')
bx, bw, bh = 8, 46, 10
ys = [62, 44, 26, 8]
labs = ['v = (2 ; 0,8)', 'T v = (−0,8 ; 2)', 'T²v = (−2 ; −0,8)', 'T²v + v = (0 ; 0)']
roles = ['sujet', 'varie', 'varie', 'resultat']
for y, lab, role in zip(ys, labs, roles):
    box(ax, bx, y, bw, bh, role, label=lab)
for y0, y1, lab in [(62, 54, 'on applique T'), (44, 36, 'on applique T'), (26, 18, 'on ajoute v')]:
    arrow(ax, (bx + bw / 2, y0), (bx + bw / 2, y1), 'varie', lw=1.2)
    text(ax, bx + bw / 2 + 4, (y0 + y1) / 2, lab, 'varie', 's', ha='left')
text(ax, bx + bw + 4, 13, "l'origine", 'resultat', 's', ha='left')
save(fig, '57-013')
