import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$p = 2$ , $M = \mathbb{Z}/4 \oplus \mathbb{Z}/2$', 'sujet', 'm')
text(ax, 44, 60, 'petit rectangle bleu = un élément', 'sujet', 's')
text(ax, 44, 55, 'cadre vert = une classe', 'resultat', 's')
rows = [(38, 'M', 8, 2, 'M(0) = M/2M\n4 classes'), (26, '2M', 2, 1, 'M(1) = 2M/4M\n2 classes'), (14, '4M', 1, 1, 'M(2) = 4M/8M\n1 classe')]
cw = 4.5
for y, lab, n, g, right in rows:
    text(ax, 2, y + 3.5, lab, 'sujet', 'm', ha='left')
    ngroups = n // g
    gw = g * cw + (g - 1) * 0.5
    for i in range(ngroups):
        gx = 13 + i * (gw + 2.4)
        for j in range(g):
            box(ax, gx + j * (cw + 0.5), y, cw, 7, 'sujet', r=0.4)
        box(ax, gx - 0.9, y - 0.9, gw + 1.8, 8.8, 'resultat', fill=False, lw=1.3, r=0.4)
    text(ax, 62, y + 3.5, right, 'resultat', 's', ha='left')
text(ax, 44, 5, r'$p\,\times$ une classe = 0 : tué par $p$', 'encre', 's')
save(fig, '60-066')
