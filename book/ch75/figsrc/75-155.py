import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y0 = 33
arrow(ax, (6, y0), (82, y0), 'fixe', lw=0.9); text(ax, 78, y0 - 3.2, 'réels', 'fixe', 's')
x0 = 56
disc(ax, x0, y0 + 16, 2, 'limite', fill=False); text(ax, x0 + 4, y0 + 16, r'$a+ib$', 'limite', 'm', ha='left')
disc(ax, x0, y0 - 16, 2, 'limite', fill=False); text(ax, x0 + 4, y0 - 16, r'$a-ib$', 'limite', 'm', ha='left')
line(ax, [(x0, y0 + 13.5), (x0, y0 - 13.5)], 'limite', dash=True)
disc(ax, x0, y0, 2.4, 'resultat'); text(ax, x0 + 4, y0 + 4, r'$H(x,x)$', 'resultat', 'm', ha='left', weight='bold')
text(ax, 4, y0 + 22, r'$H(x,x)=\overline{H(x,x)}$', 'encre', 'm', ha='left')
text(ax, 4, y0 + 15, 'donc égal à son conjugué', 'fixe', 's', ha='left')
text(ax, 4, y0 - 14, r'$b=0$ : sur les réels', 'resultat', 's', ha='left')
save(fig, '75-155')
