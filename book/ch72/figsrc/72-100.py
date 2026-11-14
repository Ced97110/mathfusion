import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
f=numberline(ax,8,76,40,-3,8,labels=False,arrow_right=False)
for v in (-3,5,7,8): pass
disc(ax,f(8),40,1.6,'sujet'); disc(ax,f(-3),40,1.6,'autre'); disc(ax,f(5),40,1.6,'fixe'); disc(ax,f(7),40,1.6,'resultat')
text(ax,f(8)+2,46,r'$x$ : 8','sujet'); text(ax,f(-3)+3,46,r'$y$ : −3','autre')
text(ax,f(5)-2,46,'carrés : 5','fixe'); text(ax,f(7)-3,56,r'$x+y$ : 7','resultat')
line(ax,[(f(7),42),(f(7),54)],'resultat',lw=0.5,dash=True)
arrow(ax,(f(8)-1.5,41.5),(f(5)+1.5,41.5),'varie',curve=0.45); text(ax,f(6.5)+4,49.5,'+(−3)','varie','s')
brace(ax,f(5),f(7),36,'varie',label='différence 2')
text(ax,44,16,r'moitié : $1=B(x,y)$','resultat','l')
text(ax,44,7,r'contrôle : $3\times1-1\times2=1$','fixe','s')
save(fig,'72-100')
