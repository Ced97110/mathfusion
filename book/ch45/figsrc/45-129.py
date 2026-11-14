import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for x0,r,head,rows,mid,verdict in [(2,'sujet','Entiers, +',('2 + 3 = 5','3 + 2 = 5'),'=','commutatif'),(46,'autre','Mots bout à bout',('ab puis ba : abba','ba puis ab : baab'),'≠','non commutatif')]:
    vr='resultat' if mid=='=' else 'limite'
    text(ax,x0+20,57,head,r,'m',weight='bold')
    box(ax,x0,40,40,10,r,label=rows[0],size='m')
    box(ax,x0,24,40,10,r,label=rows[1],size='m')
    text(ax,x0+20,37,mid,vr,'xl',weight='bold')
    text(ax,x0+20,14,verdict,vr,'m',weight='bold')
save(fig,'45-129')
