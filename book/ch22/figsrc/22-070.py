import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 14; x0 = 20; L = 3.464*u
box(ax, x0, 44, L, 8, role='varie', fill=True, label=r'$\sqrt{12}$')
text(ax, x0, 56, 'côté du grand carré', 'varie', 's', ha='left')
box(ax, x0, 26, L/2, 8, role='varie', fill=True, label=r'$\sqrt{3}$')
box(ax, x0+L/2, 26, L/2, 8, role='varie', fill=True, label=r'$\sqrt{3}$')
line(ax, [(x0+L/2, 44), (x0+L/2, 34)], 'fixe', dash=True)
brace(ax, x0, x0+L, 25, 'resultat', label=r'2 côtés $\sqrt{3}$ : $2\times\sqrt{3}$', size='m')
text(ax, 44, 9, r'$2\times1{,}732=3{,}464$', 'resultat', 'm')
save(fig, '22-070')
