import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cw,ch=22,13; ox,oy=14,26
for c in range(3): text(ax,ox+c*cw+cw/2,oy+2*ch+3.5,str(c),'autre','m')
for r in range(2): text(ax,ox-3.5,oy+(1-r)*ch+ch/2,str(r),'varie','m')
for n in range(6):
    r=n%2; c=n%3
    role='fixe'
    if r==1 and c==2: role='resultat'
    elif r==1: role='varie'
    elif c==2: role='autre'
    box(ax,ox+c*cw+0.8,oy+(1-r)*ch+0.8,cw-1.6,ch-1.6,role,label=r'$\bar{%d}$'%n,size='l')
text(ax,44,16,'ligne 1 : 5 = 2 × 2 + 1','varie','s')
text(ax,44,8,'colonne 2 : 5 = 1 × 3 + 2','autre','s')
save(fig,'52-176')
