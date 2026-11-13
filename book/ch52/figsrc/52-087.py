import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,50,'une case = une classe inversible','encre','s')
for y,k,n,t in [(30,12,4,r'$\varphi(12)=4$'),(10,7,6,r'$\varphi(7)=6$')]:
    text(ax,14,y+4,f'horloge de {k}','fixe','s')
    for i in range(n): box(ax,28+i*7.6,y,6,8,'sujet',r=0.4)
    text(ax,80,y+4,t,'resultat','m')
save(fig,'52-087')
