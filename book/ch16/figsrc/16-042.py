import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,16,60,56,11,'sujet',label=r'$5y+8=-22$',size='l')
text(ax,35,54,'gauche','fixe','s'); text(ax,65,54,'droite','fixe','s')
for y,v,l,sg,r,tag in [(38,'-6',r'$-22$',r'$=$','resultat','solution'),(18,'5',r'$33$',r'$\neq$','limite','pas solution')]:
    box(ax,2,y,18,10,'varie',label=r'$y=%s$'%v,size='m')
    box(ax,26,y,18,10,r,label=l,size='m'); text(ax,49,y+5,sg,r,'l'); box(ax,54,y,22,10,'fixe',label=r'$-22$',size='m')
    text(ax,44,y-4,tag,r,'s')
save(fig,'16-042')
