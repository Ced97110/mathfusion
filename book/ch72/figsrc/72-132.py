import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def espace(x, name):
    text(ax, x + 15, 63, name, 'sujet', 'm')
    box(ax, x, 33, 30, 20, 'sujet', label=r'$H_1$', size='l')
    box(ax, x, 21, 30, 10, 'autre', label=r'$X$', size='l')
espace(5, 'espace 1'); espace(53, 'espace 2')
text(ax, 44, 43, r'$\sim$', 'resultat', 'xl', weight='bold')
text(ax, 44, 26, r'$\sim$', 'resultat', 'xl', weight='bold')
text(ax, 20, 56.5, r'$\nu = 1$', 'sujet', 's'); text(ax, 68, 56.5, r'$\nu = 1$', 'sujet', 's')
box(ax, 4, 4, 80, 11, 'resultat', label=r"même $\nu$ et $X\sim X'$  $\Rightarrow$  espaces $\sim$", size='s')
save(fig, '72-132')
