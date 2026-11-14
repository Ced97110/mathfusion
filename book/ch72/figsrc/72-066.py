import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,75,'rotation : a = 2, déterminant 1','resultat','m',weight='bold')
for y,a,b,lab in ((63,20,40,r'$u \mapsto 2u$'),(49,20,10,r'$v \mapsto v/2$')):
    box(ax,6,y,a,8,'sujet',label='u' if y==63 else 'v')
    arrow(ax,(30,y+4),(40,y+4),'varie')
    box(ax,44,y,b,8,'resultat',label=lab if b>20 else None)
    if b<=20: text(ax,44+b+2,y+4,lab,'resultat','s',ha='left')
text(ax,44,34,'échange : déterminant −1','limite','m',weight='bold')
box(ax,6,19,20,8,'sujet',label='u'); box(ax,6,5,20,8,'autre',label='v')
box(ax,56,19,20,8,'autre',label='v'); box(ax,56,5,20,8,'sujet',label='u')
arrow(ax,(28,23),(54,9),'limite'); arrow(ax,(28,9),(54,23),'limite')
text(ax,41,29,'u ↦ v : pas un multiple de u','limite','s')
save(fig,'72-066')
