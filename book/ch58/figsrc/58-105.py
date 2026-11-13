import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# deux nombres a + b racine de 2 s'additionnent ; on en multiplie un par une fraction ; le résultat a encore deux cases a | b
BW, BH = 22.0, 10.0

def pair(x, y, a, b, role):
    """Un nombre a + b racine de 2 : une case a, une case b, séparées par un trait."""
    box(ax, x, y, BW, BH, role, label=f'{a}   |   {b}', size='m', weight='bold')

text(ax, 2 + BW / 2, 56, r'$a\ \ |\ \ b$', 'encre', 'm', ha='center')
y1 = 40
x1, x2, x3 = 2, 33, 64
pair(x1, y1, '1', '2', 'sujet')
pair(x2, y1, '3', '−1', 'autre')
pair(x3, y1, '4', '1', 'resultat')
text(ax, 28.5, y1 + BH / 2, '+', 'varie', 'l', weight='bold')
text(ax, 59.5, y1 + BH / 2, '=', 'resultat', 'l', weight='bold')
text(ax, x1 + BW / 2, y1 - 3.5, r'$1+2\sqrt{2}$', 'sujet', 's')
text(ax, x2 + BW / 2, y1 - 3.5, r'$3-\sqrt{2}$', 'autre', 's')
text(ax, x3 + BW / 2, y1 - 3.5, r'$4+\sqrt{2}$', 'resultat', 's')
y2 = 10
text(ax, 9, y2 + BH / 2, r'$\frac{1}{2}\ \times$', 'varie', 'm', weight='bold')
pair(18, y2, '1', '2', 'sujet')
text(ax, 45, y2 + BH / 2, '=', 'varie', 'l', weight='bold')
pair(52, y2, r'$\frac{1}{2}$', '1', 'varie')
text(ax, 29, y2 - 3.5, r'$1+2\sqrt{2}$', 'sujet', 's')
text(ax, 63, y2 - 3.5, r'$\frac{1}{2}+\sqrt{2}$', 'varie', 's')
line(ax, [(3, 27), (85, 27)], 'fixe', lw=0.4, dash=True)
save(fig, '58-105')
