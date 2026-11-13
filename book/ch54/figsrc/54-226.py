import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, w, bw = 22.0, 12.5, 11.0
text(ax, 11, 57, 'degré', 'fixe', 's')
rows = [(40, r'sur $\mathbb{Q}$', [True] * 5), (22, r'sur $\mathbb{R}$', [True, True, False, False, False])]
for i in range(5):
    text(ax, x0 + i * w + bw / 2, 57, str(i + 1), 'fixe', 'm')
for y, name, oks in rows:
    text(ax, 11, y + 5, name, 'encre', 's')
    for i, ok in enumerate(oks):
        x = x0 + i * w
        role = 'resultat' if ok else 'limite'
        box(ax, x, y, bw, 10, role)
        cx, cy = x + bw / 2, y + 5
        if ok:
            line(ax, [(cx - 2.5, cy), (cx - 0.8, cy - 2), (cx + 2.7, cy + 2.7)], role, lw=1.4)
        else:
            line(ax, [(cx - 2.3, cy - 2.3), (cx + 2.3, cy + 2.3)], role, lw=1.4)
            line(ax, [(cx - 2.3, cy + 2.3), (cx + 2.3, cy - 2.3)], role, lw=1.4)
text(ax, 44, 13, r'$x^3-2$ : irréductible sur $\mathbb{Q}$,', 'sujet', 's')
text(ax, 44, 7, r'il se casse sur $\mathbb{R}$', 'sujet', 's')
save(fig, '54-226')
