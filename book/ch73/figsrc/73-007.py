import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
u=18
def panel(ox,oy,steps,xa,xb):
    arrow(ax,(xa,oy),(xb,oy),"fixe",lw=0.7); arrow(ax,(ox,oy-1),(ox,oy+u+7),"fixe",lw=0.7)
    P=lambda p:(ox+p[0]*u,oy+p[1]*u)
    for i in range(len(steps)-1):
        if steps[i]!=steps[i+1]: arrow(ax,P(steps[i]),P(steps[i+1]),"varie",lw=1.1)
    for i,p in enumerate(steps):
        if i==1 and steps[1]==steps[0]: continue
        disc(ax,*P(p),1.2,"sujet" if i==0 else ("resultat" if i==len(steps)-1 else "varie"))
    return P
PA=panel(12,12,[(1,0),(1,0),(1,1),(0,1)],8,36)
PB=panel(70,12,[(0,1),(-1,1),(-1,0),(-1,0)],48,78)
text(ax,PA((1,0))[0],PA((1,0))[1]-4,'(1, 0)','sujet','s')
text(ax,PA((1,1))[0]+3,PA((1,1))[1],'(1, 1)','varie','s',ha='left')
text(ax,PA((0,1))[0]-3,PA((0,1))[1],'(0, 1)','resultat','s',ha='right')
text(ax,PB((0,1))[0]+3,PB((0,1))[1],'(0, 1)','sujet','s',ha='left')
text(ax,PB((-1,1))[0],PB((-1,1))[1]+4,'(−1, 1)','varie','s')
text(ax,PB((-1,0))[0],PB((-1,0))[1]-4,'(−1, 0)','resultat','s')
text(ax,22,42,r'$(1,0) \mapsto (0,1)$','resultat','m')
text(ax,64,42,r'$(0,1) \mapsto (-1,0)$','resultat','m')
save(fig,'73-007')
