import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, r'$\eta$ fixe les coefficients', 'fixe', 's')
text(ax, 18, 47, 'avant', 'fixe', 's')
text(ax, 70, 47, 'après', 'fixe', 's')
for x in (18, 70):
    disc(ax, x, 36, 4.5, 'sujet', label=r'$r_1$')
    disc(ax, x, 20, 4.5, 'autre', label=r'$r_2$')
arrow(ax, (22.5, 36), (65.5, 20), 'varie', lw=1.2)
arrow(ax, (22.5, 20), (65.5, 36), 'varie', lw=1.2)
text(ax, 22, 11, r'$r_1=(3+\sqrt{5})/2$', 'sujet', 's')
text(ax, 66, 11, r'$r_2=(3-\sqrt{5})/2$', 'autre', 's')
text(ax, 44, 4, r'$\eta$ : $\sqrt{5}\mapsto-\sqrt{5}$', 'varie', 's')
save(fig, '64-091')
