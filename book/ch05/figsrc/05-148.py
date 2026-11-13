import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
box(ax,2,62,41,8,'sujet',label='2 415 ÷ 105 = 23')
box(ax,45,62,41,8,'autre',label='945 ÷ 105 = 9')
s=60/24150; z=14
def panel(T,head,hrole,back,l2,endlab,endrole):
    text(ax,2,T,head,hrole,'m',ha='left')
    text(ax,z,T-5,'0','encre','s')
    y1=T-8.5; y2=T-14.5
    line(ax,[(z,T-7),(z,T-19)],'fixe',dash=True)
    xa=z+21735*s; xb=xa-back*s
    arrow(ax,(z,y1),(xa,y1),'sujet')
    text(ax,(z+xa)/2+8,T-5,'+ 23 × 945 = 21 735','sujet','s')
    arrow(ax,(xa,y2),(xb,y2),'autre')
    text(ax,(xa+xb)/2,T-18,l2,'autre','s')
    if abs(xb-z)>0.1: line(ax,[(xb,y2-2),(xb,y2+9)],hrole,dash=True)
    text(ax,2,T-22.5,endlab,endrole,'s',ha='left')
panel(56,'Avec 23 et 9','resultat',21735,'− 9 × 2 415 = − 21 735','écart 0 : le total reste 105','resultat')
panel(26,'Avec 23 et 10','limite',24150,'− 10 × 2 415 = − 24 150','le total change de −2 415','limite')
save(fig,'05-148')
