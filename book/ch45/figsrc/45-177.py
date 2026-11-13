import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx=[20,44]; cw=20; ch=6.6
text(ax,13,61,'appui','encre','s')
text(ax,30,61,r'case 1 : $r=2$','sujet','s'); text(ax,54,61,r'case 2 : $s=3$','autre','s')
for i in range(1,7):
    y=47-(i-1)*7.6
    text(ax,13,y+ch/2,str(i),'encre','m')
    box(ax,20,y,cw,ch,'resultat' if i%2==0 else 'fixe',lw=0.6,r=0.5)
    box(ax,44,y,cw,ch,'resultat' if i%3==0 else 'fixe',lw=0.6,r=0.5)
y6=47-5*7.6
box(ax,18,y6-1.5,48,ch+3,'resultat',fill=False,lw=1.6,r=0.8)
text(ax,77,y6+ch/2,'PPCM = 6','resultat','m',weight='bold')
box(ax,3,1,4,3.2,'resultat',lw=0.6,r=0.4)
text(ax,9,2.6,'vert : la case est à 0','encre','s',ha='left')
save(fig,'45-177')
