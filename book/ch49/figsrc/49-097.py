import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
xs=[12,44,76]
def row(y,seq,labs,roles,head):
    text(ax,2,y+11.5,head,'encre','m',ha='left',weight='bold')
    for i,s in enumerate(seq): disc(ax,xs[i],y,4,'resultat' if i==2 else 'fixe',label=s)
    for i in range(2):
        arrow(ax,(xs[i]+4.5,y),(xs[i+1]-4.5,y),roles[i],lw=1.3)
        text(ax,(xs[i]+xs[i+1])/2,y+6,labs[i],roles[i],'s')
text(ax,2,71,r'$g_1$ : réflexion ; $g_2$ : quart de tour','fixe','s',ha='left')
row(44,'124',['1er :\nquart de tour','2e :\nréflexion'],['varie','autre'],r'$g_1g_2x$')
row(18,'112',['1er :\nréflexion','2e :\nquart de tour'],['autre','varie'],r'$g_2g_1x$')
text(ax,44,5,"4 ≠ 2 : l'ordre compte",'limite','m',weight='bold')
save(fig,'49-097')
