import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# le signe découpé
box(ax, 14, 56, 14, 12, 'sujet', label=r'$g$', size='xl')
box(ax, 32, 56, 14, 12, 'fixe', label=r'$\neq$', size='xl')
box(ax, 50, 56, 14, 12, 'fixe', label=r'$0$', size='xl')
text(ax, 21, 50, 'diviseur', 'sujet', 's')
text(ax, 39, 50, 'n’est pas', 'fixe', 's')
text(ax, 57, 50, 'polynôme nul', 'fixe', 's')
# deux cas
box(ax, 4, 22, 38, 18, 'limite', label='', size='s')
text(ax, 23, 36, r'$g=0$', 'limite', 'm')
text(ax, 23, 28, r'degré $-\infty$ : interdit', 'limite', 's')
box(ax, 46, 22, 38, 18, 'resultat', label='', size='s')
text(ax, 65, 36, r'$g=2x-1$', 'resultat', 'm')
text(ax, 65, 28, 'degré 1 : permis', 'resultat', 's')
text(ax, 44, 10, 'un seul diviseur exclu : le polynôme nul', 'encre', 's')
save(fig, '54-150')
