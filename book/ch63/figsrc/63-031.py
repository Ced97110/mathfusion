import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 50, 40, 12, 'sujet', label=r'$(1+\sqrt{3})(2+\sqrt{3})$')
box(ax, 46, 50, 40, 12, 'varie', label=r'$(1-\sqrt{3})(2-\sqrt{3})$')
box(ax, 2, 32, 40, 12, 'resultat', label=r'$\sqrt{3}\times\sqrt{3}=3$')
box(ax, 46, 32, 40, 12, 'resultat', label=r'$(-\sqrt{3})(-\sqrt{3})=3$')
box(ax, 2, 14, 40, 12, 'sujet', label=r'$=5+3\sqrt{3}$')
box(ax, 46, 14, 40, 12, 'varie', label=r'$=5-3\sqrt{3}$')
for x in (22, 66):
    arrow(ax, (x, 50), (x, 45), 'fixe')
    arrow(ax, (x, 32), (x, 27), 'fixe')
text(ax, 44, 6, r'même fait : $(\pm\sqrt{3})^2=3$', 'resultat', 'm')
save(fig, '63-031')
