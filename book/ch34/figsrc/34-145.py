import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 60 / 1.0
x0 = 8
text(ax, 44, 57, 'angle de 30°', 'encre', 'l')
box(ax, x0, 40, 0.5 * s, 9, 'sujet', label='1er membre 0,5')
box(ax, x0, 26, 0.866 * s, 9, 'autre', label='2e membre 0,866')
line(ax, [(x0 + 0.5 * s, 36), (x0 + 0.5 * s, 49)], 'fixe', dash=True)
line(ax, [(x0 + 0.866 * s, 26), (x0 + 0.866 * s, 49)], 'fixe', dash=True)
arrow(ax, (x0 + 0.5 * s, 37.5), (x0 + 0.866 * s, 37.5), 'varie', both=True)
text(ax, x0 + 0.5 * s + 11, 43.5, 'écart', 'varie', 's')
text(ax, 44, 16, 'différence = −0,366', 'varie', 'm')
text(ax, 44, 7, '≠ 0 : égalité fausse', 'limite', 'm')
save(fig, '34-145')
