import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
R=3.6
def panel(cx,rev):
    P={'i':(cx-9,26),'j':(cx+9,26),'k':(cx,41.6)}
    def edge(a,b,role,curve=0.0,lw=1.0):
        (x0,y0),(x1,y1)=P[a],P[b]; dx,dy=x1-x0,y1-y0; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
        arrow(ax,(x0+ux*R,y0+uy*R),(x1-ux*R,y1-uy*R),role,lw=lw,curve=curve)
    edge('i','j','fixe'); edge('k','i','fixe')
    if rev: edge('j','k','fixe'); edge('k','j','varie',-0.35,1.8)
    else: edge('j','k','varie',0,1.8)
    for n in 'jk': disc(ax,*P[n],R,'sujet',label='$'+n+'$',size='l')
    disc(ax,*P['i'],R,'resultat',label='$i$',size='l')
    text(ax,P['i'][0],19.8,'le reste','resultat','s')
    text(ax,cx,11,'$kj=-i$' if rev else '$jk=i$','resultat','l')
    text(ax,cx,5.5,'contre la flèche : −' if rev else 'avec la flèche : +','varie','s')
panel(22,False); panel(66,True)
save(fig,'51-180')
