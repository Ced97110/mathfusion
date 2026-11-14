import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, x0 = 15, 8
seq = [2, -1, 0, 3, 0]
terms = ['2', '−x', None, r'$3x^3$', None]
fm = lambda v: str(v).replace('-', '−')
text(ax, 44, 57, 'suite', 'autre', 'm')
text(ax, 44, 16, 'polynôme', 'sujet', 'm')
for i, v in enumerate(seq):
    c = x0 + i * cw
    box(ax, c, 42, cw - 1.5, 9, 'autre', label=fm(v), size='m')
    arrow(ax, (c + (cw - 1.5) / 2, 41), (c + (cw - 1.5) / 2, 30.5), 'varie')
    if terms[i]:
        box(ax, c, 21, cw - 1.5, 9, 'sujet', label=terms[i], size='m')
    else:
        box(ax, c, 21, cw - 1.5, 9, 'fixe', fill=False, dash=True)
text(ax, 44, 10.5, 'le terme 0 ne s’écrit pas', 'fixe', 's')
text(ax, 44, 4, r'$2-x+3x^3$', 'resultat', 'l')
save(fig, '54-100')
