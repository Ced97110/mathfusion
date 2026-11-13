import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,14,34,26,'varie'); box(ax,52,14,34,26,'resultat')
box(ax,6,26,26,8,'varie',label=r'$(1\,3)$',size='s'); box(ax,6,16,26,8,'varie',label=r'$(1\,2\,3)$',size='s')
box(ax,56,26,26,8,'resultat',label=r'$(1\,3)$',size='s'); box(ax,56,16,26,8,'resultat',label=r'$(1\,3\,2)$',size='s')
text(ax,19,46,r'$(1\,3)K$','varie','l'); text(ax,69,46,r'$K(1\,3)$','resultat','l')
text(ax,44,27,r'$\neq$','limite','xl')
text(ax,44,6,'seul (1 3) est commun','fixe','s')
save(fig,'47-061')
