import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'12 et 18 : facteur retiré','encre','m')
rows=[('2','devient 6 et 9','encore ÷ par 3','limite','autre'),('3','devient 4 et 6','encore ÷ par 2','limite','autre'),('6','devient 2 et 3','plus de diviseur commun :\non s\'arrête','resultat','resultat')]
for i,(f,m,fl,rf,rd) in enumerate(rows):
    y=44-14*i
    disc(ax,10,y,4,rd,label=f,size='l')
    text(ax,18,y,m,'encre','m',ha='left')
    arrow(ax,(43,y),(49,y),rf)
    box(ax,50,y-5,36,10,rf,label=fl,size='s')
text(ax,44,5,'le plus grand : 6','resultat','m')
save(fig,'18-031')
