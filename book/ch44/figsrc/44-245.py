import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
cs=[15,44,73]
text(ax,cs[0],70,'a inversible','resultat','s'); text(ax,58.5,70,'a non inversible','limite','s')
line(ax,[(31,66.5),(86,66.5)],'limite')
for c,t in zip(cs,[r'$3x\equiv5$',r'$2x\equiv5$',r'$2x\equiv4$']): text(ax,c,60,t,'sujet','m')
box(ax,3,36,24,13,'resultat',label=r'$x=7$')
box(ax,32,36,24,13,'limite',fill=False,dash=True,label='aucune')
box(ax,61,36,24,13,'varie',label=r'$x=2$ et $x=6$',size='s')
V=[('existence : oui','unicité : oui','resultat','resultat'),('existence : non','','limite','limite'),('existence : oui','unicité : non','resultat','limite')]
for c,(a,b,ra,rb) in zip(cs,V):
    text(ax,c,28,a,ra,'s')
    if b: text(ax,c,20,b,rb,'s')
save(fig,'44-245')
