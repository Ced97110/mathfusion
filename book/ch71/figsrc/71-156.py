import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,54,r'forme $2xy$ : quelle flèche ?','encre','m')
o=(22,14); s=22
line(ax,[(o[0],o[1]+s),(o[0]+s,o[1]+s),(o[0]+s,o[1])],'fixe',dash=True)
arrow(ax,o,(o[0]+s,o[1]),'limite'); arrow(ax,o,(o[0],o[1]+s),'limite'); arrow(ax,o,(o[0]+s,o[1]+s),'resultat')
text(ax,o[0]+s+2,o[1],r'$e_1$ : $B=0$','limite','m',ha='left')
text(ax,o[0],o[1]+s+4,r'$e_2$ : $B=0$','limite','m')
text(ax,o[0]+s+2,o[1]+s,r'$e_1+e_2$ : $B=2$','resultat','m',ha='left')
text(ax,66,5,r'donc $u_1=e_1+e_2$','resultat','m')
save(fig,'71-156')
