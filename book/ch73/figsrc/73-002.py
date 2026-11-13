import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
b=0.25; H=30; w=4; x0=26; y0=10
line(ax,[(4,y0),(84,y0)],'fixe',lw=1.2)
text(ax,4,y0+2.6,'ligne d’écriture','fixe','s',ha='left')
poly(ax,[(x0,y0),(x0+w,y0),(x0+w,y0+H),(x0,y0+H)],'fixe',fill=False)
poly(ax,[(x0,y0),(x0+w,y0),(x0+w+b*H,y0+H),(x0+b*H,y0+H)],'sujet')
for hh,lab in [(H,'sommet : glisse le plus'),(H/2,'milieu : glisse moins')]:
    arrow(ax,(x0+w,y0+hh),(x0+w+b*hh,y0+hh),'varie')
    text(ax,x0+w+b*H+4,y0+hh,lab,'varie','s',ha='left')
text(ax,x0+2,y0-3.6,'pied : ne bouge pas','sujet','s')
text(ax,14,y0+H/2+6,'lettre droite','fixe','s')
text(ax,x0+b*H+2,y0+H+4,'italique','sujet','s')
save(fig,'73-002')
