import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
ds='00000029'; x0=6; c=9.5
for i,d in enumerate('0'+'0000029'):
    r='sujet' if d in '29' else 'fixe'
    box(ax,x0+i*c,26,c-1,12,r,label=d,size='l')
xs=lambda i:x0+i*c-0.5
disc(ax,xs(1),26.5,1.2,'varie')
disc(ax,xs(7),26.5,1.2,'resultat')
arrow(ax,(xs(7),21),(xs(1),21),'varie')
text(ax,xs(4),16,'6 rangs vers la gauche','varie','s')
brace(ax,x0+6*c,x0+8*c-1,38,'sujet',down=False,label='2 et 9 gardés')
text(ax,44,6,r'$2{,}9 \times 10^{-6}$','resultat','l',weight='bold')
save(fig,'08-095')
