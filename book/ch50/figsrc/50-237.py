import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'$|N(H\cap K)|$ : multiple de 16','encre','m')
for x,v,role,cap in [(18,'16','limite','doit dépasser 16'),(44,'32','limite','ne divise pas 48'),(70,'48','resultat',r'$N = G$')]:
    box(ax,x-10,26,20,12,role,label=v,size='l')
    text(ax,x,20,cap,role,'s')
text(ax,44,8,r'$H\cap K$ normal dans $G$','resultat','m')
save(fig,'50-237')
