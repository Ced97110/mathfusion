import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
t = 5.0
cx = [16, 44, 72]
for x, n in zip(cx, ['1', '2', '4']):
    text(ax, x, 53, n + (' carreau' if n == '1' else ' carreaux'), 'sujet' if n == '1' else 'encre', 'm')
def tiles(x, y, w, h, role):
    for i in range(w):
        for j in range(h):
            box(ax, x - w * t / 2 + i * t, y + j * t, t, t, role, r=0.3, lw=0.7)
tiles(cx[0], 36, 1, 1, 'sujet'); text(ax, cx[0], 29, 'un carré 1 × 1', 'sujet', 's')
tiles(cx[1], 36, 2, 1, 'fixe'); text(ax, cx[1], 29, 'une seule rangée', 'fixe', 's')
tiles(cx[2], 40, 4, 1, 'fixe'); tiles(cx[2], 28, 2, 2, 'fixe')
text(ax, cx[2], 22, 'deux rectangles', 'fixe', 's')
text(ax, cx[1], 14, 'premier', 'resultat', 'm'); text(ax, cx[2], 14, 'composé', 'varie', 'm')
text(ax, cx[0], 14, "ni l'un, ni l'autre", 'sujet', 's')
for x, role in zip(cx, ['sujet', 'resultat', 'varie']):
    arrow(ax, (x, 20 if x != cx[2] else 19.5), (x, 17.5), role, lw=0.9) if x != cx[2] else None
arrow(ax, (cx[0], 25.5), (cx[0], 17.5), 'sujet'); arrow(ax, (cx[1], 25.5), (cx[1], 17.5), 'resultat')
arrow(ax, (cx[2], 19.5), (cx[2], 17.5), 'varie')
save(fig, '05-051')
