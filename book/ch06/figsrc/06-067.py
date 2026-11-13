import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y=26
f=numberline(ax,8,80,y,0,3,arrow_right=False)
for v in range(4): disc(ax,f(v),y,1.5,'fixe')
for v,h in [(0.75,5),(1.25,5),(1.5,10),(1.75,5)]:
    disc(ax,f(v),y,1.5,'sujet')
text(ax,f(0.75),y+5,r'$3/4$','sujet','s'); text(ax,f(1.25),y+5,r'$5/4$','sujet','s')
text(ax,f(1.5),y+10,r'$3/2$','sujet','s'); text(ax,f(1.75),y+5,r'$7/4$','sujet','s')
brace(ax,f(1),f(2),y+16,'varie',label='aucun entier entre 1 et 2',down=False)
disc(ax,12,9,1.5,'fixe'); text(ax,16,9,'entiers','fixe','s',ha='left')
disc(ax,40,9,1.5,'sujet'); text(ax,44,9,'fractions','sujet','s',ha='left')
save(fig,'06-067')
