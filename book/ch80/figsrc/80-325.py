import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 72, r'$a \vee b = a + b + ab$', 'sujet', 'l')
text(ax, 44, 64, r'dans $\mathbb{Z}/2$ : $1 + 1 = 0$', 'varie', 'm')
for y, s in ((46, r'$1 \vee 1 = 1 + 1 + 1 = 1$'), (32, r'$1 \vee 0 = 1 + 0 + 0 = 1$'), (18, r'$0 \vee 0 = 0 + 0 + 0 = 0$')):
    box(ax, 6, y, 76, 11, 'resultat', label=s)
box(ax, 6, 3, 76, 11, 'fixe', label=r'$0 \vee 1$ : se déduit des autres', dash=True, fill=False)
save(fig, '80-325')
