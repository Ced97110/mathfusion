import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42)
f=numberline(ax,6,76,20,0,7,labels=False,arrow_right=False,role='fixe')
arrow(ax,(76,20),(84,20),'fixe',lw=0.9)
disc(ax,6,20,1.2,'fixe')
text(ax,14,33,'départ : 0 pas','fixe','s')
arrow(ax,(8,31),(6,21.5),'fixe',lw=0.6)
for v in range(7):
    arrow(ax,(f(v),21.5),(f(v+1),21.5),'varie',lw=0.9,curve=-0.5)
text(ax,14,27.5,'+1 pas','varie','s')
text(ax,71,27.5,'7e saut','varie','s')
for v in range(8):
    text(ax,f(v),16.5,str(v),'sujet','s',weight='bold' if v==7 else 'normal')
brace(ax,f(0),f(7),13,'resultat',"7 sauts depuis l'origine",down=True)
save(fig,'01-014')
