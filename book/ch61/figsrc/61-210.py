import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
y=20; u=17.5
f=numberline(ax,8,8+4*u,y,-1,3,1,arrow_right=False)
arrow(ax,(f(3),y+3),(f(3**0.5),y+3),'varie',curve=0.5)
text(ax,(f(3)+f(3**0.5))/2+1,y+13,'racine carrée','varie','s')
disc(ax,f(3),y,1.6,'sujet'); disc(ax,f(3**0.5),y,1.6,'resultat'); disc(ax,f(-1),y,1.6,'limite')
text(ax,f(3)-1,y+6.5,r'$a$ = 3','sujet','m')
text(ax,f(3**0.5)-3,y+6.5,r'$\sqrt{a}$ ≈ 1,73','resultat','m')
text(ax,3,y+16,r'$a$ < 0 : pas de $\sqrt{a}$','limite','s',ha='left')
arrow(ax,(f(-1),y+4),(f(-1),y+10),'limite')
text(ax,44,46,r'si $a$ > 0 est constructible, $\sqrt{a}$ aussi','resultat','s')
save(fig,'61-210')
