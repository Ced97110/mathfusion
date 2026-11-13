import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$28 \times 31$ : vrai produit 868', 'resultat', 'm')
rows = ((48, 'environ 900', 'one'), (34, 'près de 900', 'one'), (20, 'entre 800 et 1 000', 'two'))
for y, lab, kind in rows:
    f = numberline(ax, 8, 80, y, 800, 1000, 100, labels=False, arrow_right=False)
    text(ax, 8, y + 6, lab, 'sujet' if kind == 'two' else 'varie', 'm', ha='left')
    if kind == 'one':
        disc(ax, f(900), y, 1.6, 'varie')
    else:
        line(ax, [(f(800), y), (f(1000), y)], 'sujet', lw=2.2)
        disc(ax, f(800), y, 1.6, 'sujet'); disc(ax, f(1000), y, 1.6, 'sujet')
    disc(ax, f(868), y, 1.3, 'resultat')
for v in (800, 900, 1000): text(ax, f(v), 14.5, f'{v:,}'.replace(',', ' '), 'fixe', 's')
text(ax, 44, 6, 'un nombre, ou deux bornes', 'encre', 's')
save(fig, '10-017')
