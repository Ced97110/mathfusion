import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 28, 72, 30, 'varie', fill=False, dash=True, r=2)
for i in range(12):
    r_, c_ = divmod(i, 6)
    box(ax, 12 + c_*11.4, 46 - r_*11, 10, 8, 'sujet', label=str(i), size='s', r=0.5, lw=0.7)
text(ax, 44, 62, 'une seule classe de 12 nombres', 'varie', 's')
arrow(ax, (44, 27), (44, 17), 'encre')
box(ax, 18, 3, 52, 13, 'resultat', label=r'$G/G$ : un seul élément', size='m')
save(fig, '47-199')
