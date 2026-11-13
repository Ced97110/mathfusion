import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
P=[(r'$x^2+5x+6$',15,'sujet','départ'),(r'$=$',33,'encre',None),(r'$(x+2)$',46,'autre','diviseur'),(r'$(x+3)$',62,'resultat','quotient'),(r'$+$',72,'encre',None),(r'$0$',81,'varie','reste')]
for s,x,r,l in P:
    text(ax,x,36,s,r,'l')
    if l:
        arrow(ax,(x,26),(x,31),r); text(ax,x,20,l,r,'s')
text(ax,44,46,'dividende = diviseur × quotient + reste','encre','s')
save(fig,'21-111')
