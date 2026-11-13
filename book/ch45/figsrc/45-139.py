import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
rows=[r'$(b_1b_2)a$',r'$b_1(b_2a)$',r'$b_1(ab_2)$',r'$(b_1a)b_2$',r'$(ab_1)b_2$',r'$a(b_1b_2)$']
ys=[72-11*i for i in range(6)]
cols=['sujet']+['encre']*4+['resultat']
for y,s,c in zip(ys,rows,cols): text(ax,44,y,s,c,'m')
for i in range(5):
    key=i in (1,3); arrow(ax,(44,ys[i]-3),(44,ys[i+1]+3),'varie' if key else 'fixe')
text(ax,70,(ys[1]+ys[2])/2,r'$b_2a=ab_2$','varie','s'); text(ax,70,(ys[3]+ys[4])/2,r'$b_1a=ab_1$','varie','s')
text(ax,10,ys[0],'départ','sujet','s'); text(ax,10,ys[5],'arrivée','resultat','s')
text(ax,44,5,r"l'inverse $b^{-1}$ : même idée",'fixe','s')
save(fig,'45-139')
