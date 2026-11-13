import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 24, 36, 40, 11, 'sujet', label=r'$F$ : un corps', size='l')
for x, l in [(2, 'ℝ'), (32, 'ℂ'), (62, 'restes de ÷ 5')]:
    box(ax, x, 15, 24, 11, 'autre', label=l); arrow(ax, (44, 36), (x + 12, 26.5), 'fixe')
text(ax, 44, 6, r'on peut $+$, $-$, $\times$, $\div$', 'resultat', 'm')
save(fig, '73-118')
