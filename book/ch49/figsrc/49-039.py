import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [16, 44, 72]
titles = ['existence seule', 'unicité seule', 'les deux']
subs = ['plusieurs possibles', 'peut être vide', 'une et une seule']
roles = ['varie', 'limite', 'resultat']
for c, t, s, r in zip(cx, titles, subs, roles):
    text(ax, c, 58, t, r, 'm')
    text(ax, c, 8, s, r, 's')
    disc(ax, c - 9, 32, 3, 'sujet'); text(ax, c - 9, 24.5, 'mots', 'sujet', 's')
box(ax, 12 + 0, 0, 0, 0, 'fixe') if False else None
for c, n, r in [(cx[0], 2, 'varie'), (cx[2], 1, 'resultat')]:
    ys = [40, 24] if n == 2 else [32]
    for y in ys:
        disc(ax, c + 9, y, 3, r)
        arrow(ax, (c - 5.5, 32), (c + 5.5, y + (-0.0 if n == 1 else (1.5 if y > 32 else -1.5))), r)
disc(ax, cx[1] + 9, 32, 3, 'limite', fill=False)
text(ax, cx[1] + 9, 24.5, 'M', 'limite', 's'); text(ax, cx[0] + 9, 16.5, 'M', 'varie', 's'); text(ax, cx[2] + 9, 24.5, 'M', 'resultat', 's')
text(ax, cx[1] + 1, 32, '?', 'limite', 'l')
save(fig, '49-039')
