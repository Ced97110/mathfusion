import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0=30; u=52/24
f=lambda v: x0+v*u
rows=[(56,'multiples de 4','sujet',[4,8,12,16,20,24]),(46,'multiples de 6','autre',[6,12,18,24]),(34,'multiples de 0','fixe',[])]
line(ax,[(f(12),40),(f(12),60)],'resultat',dash=True)
for y,lab,role,vals in rows:
    text(ax,2,y,lab,role,'s',ha='left')
    disc(ax,f(0),y,1.6,'limite',fill=(y==34))
    for v in vals: disc(ax,f(v),y,1.6,'resultat' if v==12 else role)
text(ax,f(0),63,'0 exclu','limite','s')
text(ax,f(12),63,'12','resultat','s')
text(ax,36,34,'seulement 0 : pas de PPCM','limite','s',ha='left')
text(ax,34,24,r'$\mathrm{PPCM}(4,6)=12$','resultat','s',ha='left')
numberline(ax,x0,x0+52,14,0,24,step=2,every=3,arrow_right=False)
save(fig,'05-162')
