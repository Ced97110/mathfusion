import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
text(ax,44,84,r'$x\mapsto r$   et   $y\mapsto s$','encre','l')
rows=[(r'$x^4$',r'$r\,r\,r\,r$','= 1',True),(r'$y^2$',r'$s\,s$','= 1',True),(r'$xyxy$',r'$rsrs$','= 1',True),(r'$xy$',r'$rs$','réflexion',False)]
for i,(a,b,c,ok) in enumerate(rows):
    y=62-i*18; ro='resultat' if ok else 'limite'
    box(ax,4,y,22,11,'sujet' if ok else 'autre',label=a)
    arrow(ax,(27,y+5.5),(35,y+5.5),'varie')
    box(ax,36,y,26,11,'fixe',label=b)
    arrow(ax,(63,y+5.5),(68,y+5.5),ro)
    box(ax,69,y,16,11,ro,label=c,size='s')
save(fig,'49-067')
