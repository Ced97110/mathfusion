import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$p=0$ et $q=2\neq0$', 'encre', 'm')
labs = [r'$x^3+2$', r'$3x^2$', r'$-18$']
degs = ['degré 3', 'degré 2', 'degré 0']
ys = [54, 32, 8]
for y, lab, d, role in zip(ys, labs, degs, ['sujet', 'sujet', 'resultat']):
    box(ax, 30, y, 28, 11, role, label=lab)
    text(ax, 26, y + 5.5, d, 'fixe', 's', ha='right')
arrow(ax, (44, 53.5), (44, 43.5), 'varie')
text(ax, 62, 48.5, 'dérivée', 'varie', 's', ha='left')
arrow(ax, (44, 31.5), (44, 19.5), 'varie')
text(ax, 62, 25.5, r'$-9q=-9\times2$', 'varie', 's', ha='left')
save(fig, '69-126')
