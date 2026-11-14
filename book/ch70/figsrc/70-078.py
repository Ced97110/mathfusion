import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$f=y^2+x^2-4$,  $g=y+2-x^2$', 'encre', 'm')
cols = [(14, 16), (34, 16), (54, 28)]
heads = [r'$y^2$', r'$y$', r'sans $y$']
for (x, w), h in zip(cols, heads):
    text(ax, x + w / 2, 48, h, 'fixe', 'm')
text(ax, 8, 36, r'$f$', 'sujet', 'l')
text(ax, 8, 22, r'$g$', 'autre', 'l')
box(ax, 14, 31, 16, 11, 'sujet', label='1')
box(ax, 34, 31, 16, 11, 'sujet', label='0')
box(ax, 54, 31, 28, 11, 'varie', label=r'$x^2-4$')
box(ax, 34, 17, 16, 11, 'autre', label='1')
box(ax, 54, 17, 28, 11, 'varie', label=r'$2-x^2$')
text(ax, 44, 7, 'orange : contient $x$', 'varie', 's')
save(fig, '70-078')
