import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
X=lambda v:10+v*4.6
f=numberline(ax,10,79,10,0,15,labels=True,every=15,arrow_right=False)
for v in range(3,16,3): disc(ax,X(v),38,2.2,'sujet')
disc(ax,X(15),22,2.2,'autre')
line(ax,[(X(15),10),(X(15),41)],'resultat',dash=True)
text(ax,2,45,'multiples de 3, ordre de 8','sujet','s',ha='left')
text(ax,2,29,'multiples de 15, ordre de 56','autre','s',ha='left')
text(ax,44,58,'PPCM(3, 15) = 15','resultat','l')
text(ax,X(15)-2,16,'premier pas commun','resultat','s',ha='right')
save(fig,'45-241')
