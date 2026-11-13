import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,72,r'$\frac{15}{4}\times\frac{8}{5}$','sujet','l')
xs=[20,32,44,56]
for x,t in zip(xs,['3','5','2','4']): text(ax,x,50,t,'sujet','l')
for x in (26,38,50): text(ax,x,50,r'$\times$','fixe','m')
text(ax,32,32,'5','autre','l'); text(ax,56,32,'4','autre','l'); text(ax,44,32,r'$\times$','fixe','m')
line(ax,[(14,41),(62,41)],'fixe',lw=1.0)
for x in (32,56):
    line(ax,[(x,46),(x,36)],'varie',lw=1.0,dash=True)
    line(ax,[(x-2.5,53),(x+2.5,47)],'varie',lw=1.0); line(ax,[(x-2.5,35),(x+2.5,29)],'varie',lw=1.0)
text(ax,44,16,'on barre 5 ÷ 5 et 4 ÷ 4','varie','s')
text(ax,44,5,r'reste $3\times 2 = 6$','resultat','m')
save(fig,'06-074')
