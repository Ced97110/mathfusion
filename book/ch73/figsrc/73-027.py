import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 4, 40, 54, 'limite', r=1.5)
box(ax, 46, 4, 40, 54, 'resultat', r=1.5)
text(ax, 22, 53, 'toutes les matrices', 'limite', 's')
def dot(x, y, role):
    ax.add_patch(Circle((x, y), 1.0, fc=COL[role], ec=COL[role], zorder=6))
x0 = 24
p2, p1, p0 = (x0, 38), (x0, 31), (x0, 22)
dot(*p2, 'sujet'); dot(*p1, 'sujet'); dot(*p0, 'limite')
arrow(ax, (p2[0] + 1.2, p2[1] - 1.2), (p0[0] + 1.2, p0[1] + 1.4), 'limite', curve=-0.6)
arrow(ax, (p1[0], p1[1] - 1.4), (p0[0], p0[1] + 1.4), 'limite')
text(ax, x0 - 3, 38, '(3, 2)', 'sujet', 's', ha='right')
text(ax, x0 - 3, 31, '(3, 1)', 'sujet', 's', ha='right')
text(ax, x0 + 3, 17, '(3, 0)', 'limite', 's', ha='center')
text(ax, 22, 11, 'pas d’inverse : pas un groupe', 'limite', 's') if False else text(ax, 22, 9.5, 'pas d’inverse', 'limite', 's')
text(ax, 66, 54.5, 'les inversibles : un groupe', 'resultat', 's')
rows = [(36, r'$MN$ inversible', 'le produit se défait'), (21, r'$1$ : neutre', 'ne change rien'), (6, r'$M^{-1}$ existe', 'pour chaque $M$')]
for k, (y, a, b) in enumerate(rows):
    box(ax, 48, y, 36, 13, 'resultat', fill=False, lw=0.6, r=1.0)
    text(ax, 71.5, y + 8.2, a, 'resultat', 'm')
    text(ax, 71.5, y + 3.8, b, 'fixe', 's')
    ym = y + 6.5
    if k == 0:
        for x in (51.5, 56, 60.5): dot(x, ym, 'sujet')
        arrow(ax, (52.8, ym), (54.7, ym), 'varie'); arrow(ax, (57.3, ym), (59.2, ym), 'varie')
        arrow(ax, (51.8, ym + 1.2), (60.2, ym + 1.2), 'resultat', curve=-0.7)
    elif k == 1:
        dot(56, ym - 1.5, 'sujet')
        arrow(ax, (54.8, ym - 0.6), (57.2, ym - 0.6), 'fixe', curve=-2.2)
    else:
        dot(52, ym, 'sujet'); dot(60, ym, 'sujet')
        arrow(ax, (53.3, ym + 0.6), (58.7, ym + 0.6), 'varie', curve=-0.4)
        arrow(ax, (58.7, ym - 0.6), (53.3, ym - 0.6), 'resultat', curve=-0.4)
save(fig, '73-027')
