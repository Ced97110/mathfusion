import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 30, 64, 'chaque élément, 2 termes : 0', 'encre', 's')
labs = [r'$0+0=0$', r'$1+1=0$', r'$\alpha+\alpha=0$', r'$(\alpha+1)+(\alpha+1)=0$']
for i, s in enumerate(labs):
    box(ax, 3, 46 - 12 * i, 52, 9, 'resultat', label=s)
line(ax, [(57, 15.5), (57, 54.5)], 'fixe')
for i in range(4):
    line(ax, [(55, 50.5 - 12 * i), (57, 50.5 - 12 * i)], 'fixe')
arrow(ax, (57, 35), (62, 35), 'fixe')
box(ax, 62, 25, 24, 20, 'sujet', label=r'$p=2$', size='l')
text(ax, 74, 19, '2 termes suffisent', 'varie', 's')
text(ax, 74, 9, 'ordre : 4 éléments', 'autre', 's')
save(fig, '67-033')
