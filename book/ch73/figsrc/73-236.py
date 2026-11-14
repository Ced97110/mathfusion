import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def pol(o,rad,deg): return (o[0]+rad*math.cos(math.radians(deg)),o[1]+rad*math.sin(math.radians(deg)))
def arc(o,rad,a0,a1,role,head=False,lw=1.2):
    n=24; pts=[pol(o,rad,a0+(a1-a0)*i/n) for i in range(n+1)]
    line(ax,pts[:-1] if head else pts,role,lw=lw)
    if head: arrow(ax,pts[-2],pts[-1],role,lw=lw)
def panel(o,th):
    line(ax,[pol(o,17,0),pol(o,17,180)],'fixe',lw=0.8,dash=True)
    line(ax,[pol(o,17,th),pol(o,17,th+180)],'autre',lw=0.8,dash=True)
    arc(o,13,0,2*th,'resultat',head=True,lw=1.6)
    arc(o,7,0,th,'autre')
    text(ax,pol(o,10.5,th/2)[0]+1,pol(o,10.5,th/2)[1]-0.5,f'{th}°','autre','s',ha='left') if False else None
    text(ax,o[0]+20 if False else o[0],o[1]-17,'axes à 0° et %d°'%th,'autre','s')
    text(ax,o[0],o[1]+24,'rotation %d°'%(2*th),'resultat','m')
panel((22,30),45); panel((66,30),30)
text(ax,44,3,'rotation = produit de deux miroirs','resultat','s')
save(fig,'73-236')
