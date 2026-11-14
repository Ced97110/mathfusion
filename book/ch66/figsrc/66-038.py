import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'5 côtés : un facteur par racine primitive', 'sujet', 's')
bw, gap = 15, 7
x0 = (88 - (4 * bw + 3 * gap)) / 2
for i in range(4):
    x = x0 + i * (bw + gap)
    box(ax, x, 40, bw, 11, 'sujet', label=rf'$x-z_{i + 1}$')
    if i < 3: text(ax, x + bw + gap / 2, 45.5, r'$\times$', 'varie', 'm')
brace(ax, x0, x0 + 4 * bw + 3 * gap, 38, 'fixe', label='4 facteurs de degré 1')
arrow(ax, (44, 27), (44, 19), 'varie')
box(ax, 14, 4, 60, 14, 'resultat', label=r'$x\cdot x\cdot x\cdot x=x^4$ : degré 4')
save(fig, '66-038')
