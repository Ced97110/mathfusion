import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
items=[(4,26,'sujet',r'$x+3$','quantité','d\'abord'),(36,16,'varie','$=$','verbe','puis'),(62,22,'autre','7','quantité','enfin')]
for x,wd,r,l,t,o in items:
    box(ax,x,20,wd,14,r,label=l,size='l')
    text(ax,x+wd/2,15,t,r,'s')
    text(ax,x+wd/2,38.5,o,'fixe','s')
arrow(ax,(4,8),(84,8),'fixe')
text(ax,44,3,'sens de lecture','fixe','s')
save(fig,'16-033')
