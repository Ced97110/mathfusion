import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(64)
text(ax, 44, 58, 'une longueur est positive', 'sujet', 'm')
box(ax, 8, 24, 28, 28, 'fixe', label='aire 16')
line(ax, [(8, 24), (36, 24)], 'sujet', lw=2.2); line(ax, [(8, 24), (8, 52)], 'sujet', lw=2.2)
brace(ax, 8, 36, 24, 'sujet', r'$4$ m', True, 'm')
box(ax, 54, 28, 26, 16, 'limite', fill=False, dash=True, label=r'côté $-4$ m', size='s')
text(ax, 67, 22, "n'existe pas", 'limite', 's')
save(fig, '22-038')
