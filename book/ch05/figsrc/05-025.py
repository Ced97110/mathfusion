import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y=22
f=numberline(ax,6,74,y,0,25,labels=False,arrow_right=False)
for v in (0,3,8,13,18,23): text(ax,f(v),y-3.6,f'{v}','encre','s')
for a in (23,18,13,8): arrow(ax,(f(a),y+1.5),(f(a-5),y+1.5),'varie',curve=0.5)
disc(ax,f(23),y,1.5,'sujet'); disc(ax,f(3),y,1.5,'resultat')
text(ax,40,33,'on retire 5, quatre fois : $q=4$','varie','m')
brace(ax,f(0),f(3),11,'resultat',label=r'$r=3$'); brace(ax,f(3),f(23),11,'fixe',label=r'$5\times 4=20$')
text(ax,44,58,r'$a=23,\ b=5$','sujet','m')
text(ax,44,50,r'$23=5\times 4+3$','resultat','l')
text(ax,44,43,r'$0\leq 3<5$','resultat','m')
save(fig,'05-025')
