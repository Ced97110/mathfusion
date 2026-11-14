import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 14
x0, y0 = 5, 18
poly(ax, [(x0, y0), (x0 + s, y0), (x0 + s, y0 + s)], 'sujet')
poly(ax, [(x0, y0), (x0 + s, y0 + s), (x0, y0 + s)], 'sujet')
text(ax, x0 + s * 2 / 3 + 0.5, y0 + s / 3 - 0.5, '1/2', 'sujet', 's')
text(ax, x0 + s / 3 - 0.5, y0 + s * 2 / 3 + 0.5, '1/2', 'sujet', 's')
text(ax, x0 + s / 2, y0 - 4, 'carré bleu : aire 1', 'sujet', 's')
cx, cy = 58, 26
tri = [((cx, cy), (cx + s, cy), (cx, cy + s)), ((cx, cy), (cx, cy + s), (cx - s, cy)),
       ((cx, cy), (cx - s, cy), (cx, cy - s)), ((cx, cy), (cx, cy - s), (cx + s, cy))]
for t in tri:
    poly(ax, list(t), 'varie')
    text(ax, (t[0][0] + t[1][0] + t[2][0]) / 3, (t[0][1] + t[1][1] + t[2][1]) / 3, '1/2', 'varie', 's')
line(ax, [(cx + s, cy), (cx, cy + s), (cx - s, cy), (cx, cy - s), (cx + s, cy)], 'varie', lw=1.2, dash=True)
text(ax, cx, cy - s - 4, 'carré orange', 'varie', 's')
arrow(ax, (x0 + s + 3, y0 + s / 2), (cx - s - 3, y0 + s / 2), 'fixe')
box(ax, 18, 47, 52, 9, 'resultat', label=r'$4\times 1/2 = 2$')
save(fig, '22-017')
