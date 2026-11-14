import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
vals=[('-2','4','varie'),('6','36','sujet'),('-3','9','sujet'),('1','1','sujet')]
for i,(a,b,r) in enumerate(vals):
    x=3+i*21
    box(ax,x,40,19,12,r,label=r'$%s$'%a,size='l')
    text(ax,x+9.5,34,r'$(%s)^{2}=%s$'%(a,b),r,'s')
text(ax,12.5,57,'partie réelle','varie','s')
brace(ax,24,84,55,'sujet',None,down=False,depth=1.6)
text(ax,54,62,r'partie vectorielle : $36+9+1=46$','sujet','s')
box(ax,6,6,76,13,'resultat',label=r'$4+46=50=5\times10$',size='l')
arrow(ax,(44,30),(44,20),'resultat')
save(fig,'78-127')
