import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
X=[40,56,72]; top=['1','2','3']; bot=['2','3','1']
text(ax,2,52,'départ','fixe','s',ha='left'); text(ax,2,26,'arrivée','resultat','s',ha='left')
for x,a,b in zip(X,top,bot):
    box(ax,x-6,47,12,10,'fixe',label=a); box(ax,x-6,21,12,10,'resultat',label=b)
    arrow(ax,(x,46.4),(x,31.6),'varie')
    text(ax,x,12,f'$\\pi({a})={b}$','varie','s')
text(ax,56,63,r'on lit par colonne','sujet','m')
save(fig,'42-249')
