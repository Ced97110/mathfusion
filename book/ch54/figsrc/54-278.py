import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, w, lab, role in [(2, 24, 'corps de départ', 'sujet'), (32, 26, 'polynôme irréductible', 'varie'), (64, 22, 'corps obtenu', 'resultat')]:
    text(ax, x + w / 2, 60, lab, role, 's')
data = [(42, 'ℝ', r'$x^2+1$', 'ℂ'), (14, 'ℤ/3', r'$x^3+x^2+2$', '27 éléments')]
for y, a, p, c in data:
    box(ax, 2, y, 24, 11, 'sujet', label=a, size='m')
    box(ax, 32, y, 26, 11, 'varie', label=p, size='s')
    box(ax, 64, y, 22, 11, 'resultat', label=c, size='s')
    text(ax, 29, y + 5.5, '+', 'encre', 'l')
    arrow(ax, (58, y + 5.5), (64, y + 5.5), 'resultat')
text(ax, 44, 5, 'quotient : un corps', 'resultat', 's')
save(fig, '54-278')
