import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$a=-2$ ; $b=3$ ; $ab=-6$', 'encre', 's')
c = 8; x0, y0 = 16, 14
for i in range(2):
    for j in range(3):
        poly(ax, [(x0 + i * c, y0 + j * c), (x0 + (i + 1) * c, y0 + j * c),
                  (x0 + (i + 1) * c, y0 + (j + 1) * c), (x0 + i * c, y0 + (j + 1) * c)], 'sujet')
brace(ax, x0, x0 + 2 * c, y0 - 0.5, 'sujet', label=r'$|a|=2$')
text(ax, 9, y0 + 12, r'$|b|=3$', 'sujet', 's', rot=90)
box(ax, 42, 38, 44, 11, 'sujet', label=r'$|ab|=|-6|=6$', size='s')
text(ax, 64, 32, '=', 'resultat', 'xl')
box(ax, 42, 14, 44, 11, 'sujet', label=r'$|a|\times|b|=2\times 3=6$', size='s')
save(fig, '69-038')
