import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
vals = ['3', '5', '17', '257', '65 537']
w, g = 9.2, 1.3
x0 = 3
for i, v in enumerate(vals):
    box(ax, x0 + i * (w + g), 22, w, 10, 'resultat', label=v, size='s', r=0.6)
x5 = x0 + 5 * (w + g)
box(ax, x5, 22, w, 10, 'limite', label=r'$F_5$', size='s', r=0.6)
box(ax, x5 + (w + g), 22, w, 10, 'fixe', label='?', size='m', dash=True, r=0.6)
box(ax, x5 + 2 * (w + g), 22, w, 10, 'fixe', label='?', size='m', dash=True, r=0.6)
brace(ax, x0, x0 + 4 * (w + g) + w, 20, 'resultat', 'cinq premiers connus')
brace(ax, x5, x5 + w, 20, 'limite', 'composé')
brace(ax, x5 + (w + g), x5 + 2 * (w + g) + w, 20, 'fixe', 'on ignore')
text(ax, 44, 44, 'un sixième premier de Fermat ?', 'encre', 'm')
save(fig, '66-072')
