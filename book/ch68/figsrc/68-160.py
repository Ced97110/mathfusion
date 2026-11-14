import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
text(ax, 44, 79, r'$C$ = {000, 111}', 'sujet', 'm')
def add(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
for i, e in enumerate(['000', '100', '010', '001']):
    y = 62 - i * 14
    box(ax, 3, y, 18, 8, 'fixe' if e == '000' else 'varie', label=rf'$e$ = {e}')
    text(ax, 31, y + 4, r'$+\, C \rightarrow$', 'encre', 's')
    box(ax, 41, y - 2, 44, 12, 'sujet', fill=False, dash=True)
    box(ax, 44, y, 17, 8, 'sujet', label=add(e, '000'))
    box(ax, 65, y, 17, 8, 'sujet', label=add(e, '111'))
text(ax, 44, 8, '4 classes × 2 mots = 8 mots', 'encre', 's')
save(fig, '68-160')
