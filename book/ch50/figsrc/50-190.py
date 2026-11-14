import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 12, 68, r'$|HK|$', 'resultat', 'xl'); text(ax, 22, 68, '=', 'encre', 'xl')
text(ax, 37, 72, r'$|H|$', 'sujet', 'xl'); text(ax, 45, 72, r'$\times$', 'encre', 'xl'); text(ax, 53, 72, r'$|K|$', 'autre', 'xl')
line(ax, [(29, 68), (61, 68)], 'encre', lw=1.0)
text(ax, 45, 63, r'$|H \cap K|$', 'fixe', 'xl')
def venn(cx, y, ho, sh, ko, lab):
    disc(ax, cx - 5, y, 9, 'sujet', fill=False, lw=1.1); disc(ax, cx + 5, y, 9, 'autre', fill=False, lw=1.1)
    for (p, r) in ([(q, 'sujet') for q in ho] + [(q, 'fixe') for q in sh] + [(q, 'autre') for q in ko]):
        disc(ax, cx + p[0], y + p[1], 1.3, r)
    text(ax, cx - 9, y + 12.5, r'$H$', 'sujet', 'm'); text(ax, cx + 9, y + 12.5, r'$K$', 'autre', 'm')
    text(ax, cx, y - 14, lab, 'resultat', 'm')
venn(22, 34, [(-9, 3), (-9, -3)], [(0, 0)], [(9, 0)], r'$3 \times 2 / 1 = 6$')
venn(66, 34, [(-9, 3), (-9, -3)], [(0, 2.2), (0, -2.2)], [(7.5, 3.5), (7.5, -3.5), (10.5, 3.5), (10.5, -3.5)], r'$4 \times 6 / 2 = 12$')
save(fig, '50-190')
