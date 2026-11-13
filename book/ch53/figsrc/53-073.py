import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
x0, w, g, y, h = 4, 8, 1, 30, 9
step = w + g
for i in range(9):
    box(ax, x0 + i * step, y, w, h, 'sujet', label=rf'$k_{i % 3 + 1}$')
for t, nom in enumerate(['1er', '2e', '3e']):
    xa = x0 + t * 3 * step
    brace(ax, xa, xa + 3 * w + 2 * g, y - 1, 'fixe', label=f'{nom} passage')
for t in range(2):
    pa = (x0 + t * 3 * step + w / 2, y + h + 0.5)
    pb = (x0 + (t + 1) * 3 * step + w / 2, y + h + 0.5)
    arrow(ax, pa, pb, 'varie', curve=-0.5)
text(ax, 44, y + h + 9, 'la clé revient', 'varie', 'm')
arrow(ax, (44, y - 9), (44, 14), 'resultat')
box(ax, 14, 3, 60, 10, 'resultat', label='Kasiski casse ce chiffre')
save(fig, '53-073')
