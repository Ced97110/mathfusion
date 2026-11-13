import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(75)
ys=[52,55,58,61,64]; xs=[25,27,27.8,27,25]
c=np.polyfit(ys,xs,2); yy=np.linspace(52,64,40)
line(ax,list(zip(np.polyval(c,yy),yy)),'sujet',lw=1.4)
text(ax,19,58,'8','sujet','l'); text(ax,15,49,r'diviseur $d$','sujet','s')
for x,d in zip([34.5,43.5,52.5,61.5],'4944'): text(ax,x,58,d,'sujet','l')
text(ax,77,58,r'dividende $n$','sujet','s')
for x in (30,39,48,57,66): line(ax,[(x,24),(x,66)],'fixe',lw=0.5,dash=True)
for x,s in zip([34.5,43.5,52.5,61.5],['mil.','cent.','diz.','un.']): text(ax,x,69,s,'fixe','s')
for y in (44,35,26): box(ax,31,y,34,5,'fixe',fill=False,dash=True,lw=0.6)
text(ax,14,38,'place des','fixe','s'); text(ax,14,34,'soustractions','fixe','s')
arrow(ax,(23,36),(30,37.5),'fixe',lw=0.6)
arrow(ax,(71,48),(71,26),'varie')
text(ax,44,13,'la place remplace les mots','resultat','m')
save(fig,'03-048')
