import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, ch = 16, 11
cx = [30, 58]
box(ax, 20, 4, 36, 0.1, 'fixe') if False else None
text(ax, cx[0] + cw / 2, 74, r'dans $G$', 'sujet', 'm'); text(ax, cx[1] + cw / 2, 74, r'dans $H$', 'autre', 'm')
rows = [(58, 1, 1, 'sujet', 'autre'), (42, 1, 2, 'sujet', 'autre'), (24, 0, 0, 'resultat', 'resultat')]
for y, a, b, ra, rb in rows:
    box(ax, cx[0], y, cw, ch, ra, label=str(a), size='l'); box(ax, cx[1], y, cw, ch, rb, label=str(b), size='l')
text(ax, 20, 47.5, '+', 'varie', 'xl'); text(ax, 20, 29.5, '=', 'varie', 'xl')
line(ax, [(cx[0] - 4, 38), (cx[1] + cw + 4, 38)], 'fixe')
text(ax, cx[0] + cw / 2, 15, '1+1=2, reste 0', 'sujet', 's'); text(ax, cx[1] + cw / 2, 15, '1+2=3, reste 0', 'autre', 's')
save(fig, '45-155')
