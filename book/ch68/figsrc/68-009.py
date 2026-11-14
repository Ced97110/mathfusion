import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
copies = ['0110', '1110', '0110']
for r, (y, w) in enumerate(zip([46, 34, 22], copies)):
    for i, b in enumerate(w):
        bad = (r == 1 and i == 0)
        box(ax, 21 + i * 12, y, 10, 9, 'varie' if bad else 'sujet', label=b, size='l')
text(ax, 10, 38.5, 'bit 5\ninversé', 'varie', 's')
arrow(ax, (16.5, 38.5), (20.5, 38.5), 'varie')
arrow(ax, (44, 21.5), (44, 14.6), 'resultat')
box(ax, 21, 5, 46, 9, 'resultat', label='majorité : 0110', size='m')
save(fig, '68-009')
