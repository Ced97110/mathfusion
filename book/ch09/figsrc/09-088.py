import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
xs=[14,28,42,56,70]
for x,s in zip([14,42,70],['P','Q','B']): box(ax,x-7,62,14,10,'sujet',label=f'${s}$')
text(ax,28,67,'=','encre','l'); text(ax,56,67,'×','encre','l')
rows=[('15','0,30','50'),('16','0,20','80'),('6','0,50','12')]
for r,(p,q,b) in zip([46,30,14],rows):
    box(ax,7,r,14,10,'resultat',label=p); box(ax,35,r,14,10,'varie',label=q); box(ax,63,r,14,10,'varie',label=b)
save(fig,'09-088')
