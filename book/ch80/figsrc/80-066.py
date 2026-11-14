import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(84)
text(ax,44,79,r'loi : $W\wedge(U\vee X)=U\vee(W\wedge X)$','encre','m')
text(ax,44,72,r'vraie si $U\subseteq W$ ; ici $U\not\subseteq W$','encre','s')
ox,oy,r=26,40,21
poly(ax,[(ox-r,oy-r),(ox+r,oy-r),(ox+r,oy+r),(ox-r,oy+r)],'fixe')
for ang,role,n in ((0,'sujet','U'),(60,'autre','W'),(120,'varie','X')):
    c,sn=math.cos(math.radians(ang)),math.sin(math.radians(ang)); k=r*0.95/max(abs(c),abs(sn))*0.95
    line(ax,[(ox-c*k,oy-sn*k),(ox+c*k,oy+sn*k)],role,lw=2.0)
    text(ax,ox+c*k*0.80+ (3 if ang!=120 else -3),oy+sn*k*0.80+(3 if ang==0 else 0),n,role,'m')
disc(ax,ox,oy,1.0,'encre')
text(ax,68,58,'côté gauche','fixe','s')
text(ax,68,51,r'$W\wedge(U\vee X)=W$','autre','s')
text(ax,68,40,'côté droit','fixe','s')
text(ax,68,33,r'$U\vee(W\wedge X)=U$','sujet','s')
text(ax,68,21,r'$W=U$ : faux','limite','l')
text(ax,68,13,'la loi échoue','limite','s')
text(ax,44,5,'trois droites distinctes du plan','encre','s')
save(fig,'80-066')
