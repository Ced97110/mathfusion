import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 6, 52, 76, 10, 'sujet', label=r'$6x^2+5x+1=(2x+1)(3x+1)$', size='m')
f = numberline(ax, 14, 74, 32, -1, 0, step=1, arrow_right=False, size='m', tick=1.6)
for v, lab in [(-0.5, '−1/2'), (-1 / 3, '−1/3')]:
    disc(ax, f(v), 32, 1.5, 'sujet')
    text(ax, f(v), 37.5, lab, 'sujet', 's')
    arrow(ax, (f(v), 36), (f(v), 33.8), 'sujet', lw=0.7)
text(ax, 44, 22, 'aucune racine entière', 'fixe', 's')
box(ax, 4, 4, 38, 11, 'limite', label='critère : « irréductible »', size='s')
box(ax, 46, 4, 38, 11, 'varie', label='mais il se casse', size='s')
text(ax, 44, 9.5, '≠', 'encre', 'l', weight='bold')
save(fig, '54-205')
