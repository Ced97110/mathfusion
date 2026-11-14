import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,4,46,r'$7 \div 4 = 1{,}75$','encre','m',ha='left')
box(ax,50,40,18,9,'resultat',label='reste 0',size='s')
text(ax,77,44.5,'terminée','resultat','s')
text(ax,4,22,r'$1 \div 3 = 0{,}333\ldots$','encre','m',ha='left')
for i in range(3):
    box(ax,4+i*14,6,12,9,'varie',label='1',size='s')
text(ax,4+3*14+4,10.5,r'$\ldots$','varie','l')
text(ax,18,2.5,'restes','varie','s')
text(ax,70,13,'non terminée :','varie','s'); text(ax,70,8,'jamais 0','limite','s')
save(fig,'08-073')
