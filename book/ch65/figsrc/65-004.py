import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 14, 68, 'une racine', 'sujet', 's')
text(ax, 68, 68, 'son image par $\\eta$', 'varie', 's')
box(ax, 2, 40, 24, 12, 'sujet', label='1,41', size='l')
text(ax, 14, 35, r'$1{,}41^2\approx2$', 'sujet', 's')
targets = [(58, 'resultat', '1,41', r'$1{,}41^2\approx2$'), (36, 'resultat', '−1,41', r'$(-1{,}41)^2\approx2$'), (14, 'limite', '3', r'$3^2-2=7\neq0$')]
for y, role, lab, calc in targets:
    box(ax, 56, y - 6, 20, 12, role, label=lab, size='m', dash=(role == 'limite'))
    arrow(ax, (26, 46), (56, y), 'limite' if role == 'limite' else 'varie')
    text(ax, 66, y - 9, calc, role, 's')
text(ax, 40, 56, r'$\eta$', 'varie', 'l')
text(ax, 34, 20, 'impossible', 'limite', 's')
save(fig, '65-004')
