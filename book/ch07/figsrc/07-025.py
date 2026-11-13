import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(84)
text(ax,44,79,'7/15 − 4/15 = 3/15','resultat','l')
row(ax,11,56,4.4,8,['resultat']*3+['varie']*4+['fixe']*8)
brace(ax,11,24.2,56,'resultat','3 restent')
brace(ax,24.2,41.8,64,'varie','4 retirées',down=False)
text(ax,44,40,'même calcul, règle fausse','limite','s')
text(ax,44,33,'haut : 7 − 4 = 3','limite','s')
text(ax,44,26,'bas : 15 − 15 = 0','limite','s')
arrow(ax,(44,23),(44,16),'limite')
box(ax,16,4,56,11,'limite',label='3/0 n’existe pas',size='m')
save(fig,'07-025')
