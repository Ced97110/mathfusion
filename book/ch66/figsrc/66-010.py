import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
poly(ax, [(6, 36), (26, 36), (26, 56), (6, 56)], 'sujet')
line(ax, [(6, 36), (26, 56)], 'varie', lw=1.4)
text(ax, 16, 31.5, 'côté 1', 'sujet', 's')
text(ax, 21.5, 42.5, r'$d$', 'varie', 'm')
text(ax, 16, 22, r'$d^2=2$', 'varie', 'm')
text(ax, 16, 15, 'équation de degré 2', 'varie', 's')
def row(y, kind):
    if kind == 0:
        line(ax, [(46, y - 6), (62, y + 6)], 'sujet'); line(ax, [(46, y + 6), (62, y - 6)], 'sujet')
        pts = [(54, y)]; t = 'droite + droite'; d = 1
    elif kind == 1:
        disc(ax, 54, y, 6, 'sujet', fill=False); line(ax, [(44, y + 2), (64, y + 2)], 'sujet')
        k = math.sqrt(36 - 4); pts = [(54 - k, y + 2), (54 + k, y + 2)]; t = 'droite + cercle'; d = 2
    else:
        disc(ax, 51, y, 6, 'sujet', fill=False); disc(ax, 57, y, 6, 'sujet', fill=False)
        k = math.sqrt(36 - 9); pts = [(54, y + k), (54, y - k)]; t = 'cercle + cercle'; d = 2
    for p in pts: disc(ax, p[0], p[1], 1.1, 'resultat')
    text(ax, 67, y + 3, t, 'sujet', 's', ha='left'); text(ax, 67, y - 3, 'degré %d' % d, 'varie', 's', ha='left')
row(66, 0); row(44, 1); row(22, 2)
save(fig, '66-010')
