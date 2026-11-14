import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$16x^5-9x^4+3x^2+6x-21$', 'sujet', 'l')
text(ax, 44, 72, 'nombre premier  p = 3', 'encre', 'm')
vals = ['16', '−9', '0', '3', '6', '−21']
w = 13.0
x0 = 5.0
for i, v in enumerate(vals):
    box(ax, x0 + i * w, 54, w - 1.0, 10, 'varie' if i == 0 else 'sujet', label=v, size='m')
brace(ax, x0 + w, x0 + 6 * w - 1, 52, 'sujet', depth=1.8)
# trois conditions alignées, chacune cochée
conds = [('varie', '✓  16 n’est pas divisible par 3'),
         ('sujet', '✓  tous les autres sont divisibles par 3'),
         ('sujet', '✓  9 ne divise pas −21')]
for k, (rl, s) in enumerate(conds):
    box(ax, 4, 40 - k * 10, 80, 8, rl, label=s, size='s')
box(ax, 14, 3, 60, 10, 'resultat', label=r'donc irréductible sur $\mathbb{Q}$', size='m')
save(fig, '54-223')
