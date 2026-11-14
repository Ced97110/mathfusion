import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
X=[14,44,74]; y=58
for x,l,r in zip(X,['1','2','4'],['sujet','fixe','fixe']): disc(ax,x,y,4.2,r,label=l)
for i,l in enumerate([r'$\alpha$ : +1',r'$\beta$ : ×2']):
    arrow(ax,(X[i]+4.8,y),(X[i+1]-4.8,y),'fixe',curve=-0.35); text(ax,(X[i]+X[i+1])/2,y+9,l,'fixe','s')
for i,l in ((1,r'$\beta^{-1}$ : ÷2'),(0,r'$\alpha^{-1}$ : −1')):
    arrow(ax,(X[i+1]-4.8,y),(X[i]+4.8,y),'resultat',curve=-0.35); text(ax,(X[i]+X[i+1])/2,y-9.5,l,'resultat','s')
text(ax,44,80,'retour : on défait β d’abord','resultat','m')
y2=24
for x,l,r in zip(X,['4','3','1,5'],['fixe','fixe','limite']): disc(ax,x,y2,4.2,r,label=l,size='s' if l=='1,5' else 'm')
for i,l in enumerate(['−1','÷2']):
    arrow(ax,(X[i]+4.8,y2),(X[i+1]-4.8,y2),'limite'); text(ax,(X[i]+X[i+1])/2,y2+4,l,'limite','s')
text(ax,44,10,'ordre gardé : 1,5, pas 1','limite','m')
save(fig,'42-244')
