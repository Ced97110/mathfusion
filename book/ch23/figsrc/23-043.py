import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 3.5; s = 22; b = 3 * u; y0 = 14
for ox in (3, 50):
    box(ax, ox, y0 + b, s, s, 'sujet', label='x²')
    box(ax, ox + s, y0 + b, b, s, 'fixe', label='3x', size='s')
    box(ax, ox, y0, s, b, 'fixe', label='3x', size='s')
box(ax, 3 + s, y0, b, b, 'varie', fill=False, dash=True)
box(ax, 50 + s, y0, b, b, 'varie', label='9', size='s')
arrow(ax, (37, y0 + 16), (48, y0 + 16), 'varie'); text(ax, 42.5, y0 + 21, '+ 9', 'varie', 's')
text(ax, 19, 8, 'carré incomplet', 'sujet', 's')
text(ax, 66, 8, 'carré complet', 'resultat', 's')
brace(ax, 50, 50 + s + b, y0 + s + b + 1, 'resultat', label='x + 3', down=False)
save(fig, '23-043')
