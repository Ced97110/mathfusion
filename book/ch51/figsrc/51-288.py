import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
box(ax, 4, 18, 18, 12, 'sujet', label=r'$\alpha$', size='l')
text(ax, 13, 44, 'le réel', 'sujet', 'm')
text(ax, 29, 24, r'$=$', 'encre', 'l')
x0, y0, cw, ch = 40, 12, 14, 12
vals = [[r'$\alpha$', '0'], ['0', r'$\alpha$']]
for r in range(2):
    for c in range(2):
        role = 'sujet' if r == c else 'fixe'
        box(ax, x0 + c*cw, y0 + (1-r)*ch, cw, ch, role, label=vals[r][c])
for sx, d in ((x0 - 1.5, 1), (x0 + 2*cw + 1.5, -1)):
    line(ax, [(sx + d*1.5, y0 - 1), (sx, y0 - 1), (sx, y0 + 2*ch + 1), (sx + d*1.5, y0 + 2*ch + 1)], 'encre')
line(ax, [(x0 + 1.5, y0 + 2*ch - 1.5), (x0 + 2*cw - 1.5, y0 + 1.5)], 'varie', dash=True)
text(ax, x0 + cw, 44, 'matrice diagonale', 'sujet', 'm')
text(ax, x0 + cw, 5, 'α deux fois, en diagonale', 'varie', 's')
save(fig, '51-288')
