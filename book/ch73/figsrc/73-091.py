import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 76 / 80; x = 6; y = 26; h = 10
parts = [(25, 'sujet', r'$\|x\|^2$', '25'), (15, 'varie', r'$\langle x,y\rangle$', '15'), (15, 'varie', r'$\langle y,x\rangle$', '15'), (25, 'autre', r'$\|y\|^2$', '25')]
xs = []
for v, role, sym, num in parts:
    box(ax, x, y, v * s, h, role, label=num, r=0.5)
    text(ax, x + v * s / 2, y + h + 4, sym, role, 's')
    xs.append((x, x + v * s)); x += v * s
text(ax, 44, 59, r'$\langle x+y,\,x+y\rangle=80$', 'encre', 'm')
arrow(ax, (44, 54), (44, 44), 'varie', lw=1.2)
text(ax, 48, 49, 'développer', 'varie', 's', ha='left')
brace(ax, xs[1][0], xs[2][1], y, 'varie', label='égaux : 2 × 15 = 30')
text(ax, 44, 8, '25 + 30 + 25 = 80', 'resultat', 'm')
save(fig, '73-091')
