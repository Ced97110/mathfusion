import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
for i in range(10): box(ax,4+8*i,40,7,8,'sujet',label=str(i),size='l')
box(ax,48,18,30,9,'sujet',label='4 329',size='l')
for d,t in ((4,54),(3,61),(2,66),(9,71)):
    line(ax,[(4+8*d+3.5,40),(t,27)],'sujet',lw=0.6)
box(ax,8,18,24,9,'autre',label='chat',size='l')
text(ax,20,11,'4 lettres : un mot','resultat','s')
text(ax,63,11,'4 chiffres : un nombre','resultat','s')
save(fig,'01-017')
