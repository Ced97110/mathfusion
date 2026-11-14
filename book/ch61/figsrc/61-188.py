import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,44,62,r'$\mathbb{Q}(\sqrt[3]{2})$ : trois briques','sujet')
for x,l in zip([8,32,56],['1',r'$\sqrt[3]{2}$',r'$(\sqrt[3]{2})^2$']):
    box(ax,x,46,24,12,'sujet',label=l,size='s')
brace(ax,8,80,46,'sujet','degré 3')
for i,k in enumerate([1,2,3,4]):
    ok=k!=3
    box(ax,8+20*i,18,16,10,'resultat' if ok else 'limite',label=str(k),size='m')
arrow(ax,(52,37),(56,29),'varie')
text(ax,56,12,'pas une puissance de 2','limite','s')
text(ax,44,5,r'donc $\sqrt[3]{2}$ non constructible','limite','s')
save(fig,'61-188')
