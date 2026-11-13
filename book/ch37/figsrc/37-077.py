import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
D = math.sqrt(984375)
k, y0 = 0.68, 10
specs = [(6, 35, 'fixe', 'a'), (37.8, 25, 'sujet', 'b'), (62.8, 15, 'autre', 'c')]
fig, ax = canvas(68)
for x, f, role, L in specs:
    r = D / f; w, h = f*k, r*k
    box(ax, x, y0, w, h, role, r=0.4)
    text(ax, x + w/2, y0 + h/2, '992,2', role, 'm')
    text(ax, x + w/2, y0 + h + 3, rf'$r_{L}$ = {r:.2f}'.replace('.', ','), role, 'm')
    text(ax, x + w/2, y0 - 3, rf'$s-{L}$ = {f}', role, 'm')
text(ax, 44, 64, 'hauteur r × largeur (s − côté)', 'resultat', 'm', weight='bold')
save(fig, '37-077')
