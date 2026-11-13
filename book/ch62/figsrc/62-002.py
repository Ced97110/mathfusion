import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, cw, ch = 22, 21.5, 14
cols = ['fractions', 'réels', 'autre corps']
for i, c in enumerate(cols):
    text(ax, x0 + i * cw + cw / 2, 56, c, 'sujet', 's')
text(ax, 11, 40.5, 'degré 2', 'fixe', 's')
text(ax, 11, 26, 'degré > 2', 'fixe', 's')
# row degré 2 : two cases already seen, one open
box(ax, x0, 33, cw - 1.5, ch, 'resultat', label='$x^2-2$\nvu', size='s')
box(ax, x0 + cw, 33, cw - 1.5, ch, 'resultat', label='$x^2+1$\nvu', size='s')
box(ax, x0 + 2 * cw, 33, cw - 1.5, ch, 'varie', label='?', size='l', dash=True)
for i in range(3):
    box(ax, x0 + i * cw, 17, cw - 1.5, ch, 'varie', label='?', size='l', dash=True)
text(ax, 44, 8, 'le geste vaut-il pour toutes les cases ?', 'encre', 'm')
save(fig, '62-002')
