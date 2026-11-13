import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,24,52,r'$\frac{3}{4}$','sujet','xl'); text(ax,24,28,r'$\frac{1}{4}$','autre','xl')
line(ax,[(8,40),(40,40)],'varie',lw=1.6)
text(ax,24,60,'haut : fraction','sujet','s'); text(ax,24,20,'bas : fraction','autre','s')
text(ax,48,40,'=','encre','l')
text(ax,67,46,r'$3/4 \div 1/4$','varie','m'); text(ax,67,34,'= 3','resultat','l')
text(ax,44,8,'la grande barre veut dire ÷','varie','s')
save(fig,'06-080')
