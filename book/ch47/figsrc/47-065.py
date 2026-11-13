import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
L=[('1, (1 2)','sujet'),('(1 3), (1 2 3)','varie'),('(2 3), (1 3 2)','varie')]
R=[('1, (1 2)','sujet'),('(2 3), (1 2 3)','autre'),('(1 3), (1 3 2)','autre')]
text(ax,21,60,'à gauche','varie','l'); text(ax,67,60,'à droite','autre','l')
for i,((a,ra),(b,rb)) in enumerate(zip(L,R)):
    y=44-i*15
    box(ax,2,y,38,11,ra,label=a); box(ax,48,y,38,11,rb,label=b)
    if i==0: text(ax,44,y+5.5,'=','resultat','l')
    else: text(ax,44,y+5.5,r'$\neq$','limite','l')
text(ax,44,6,'3 paires de chaque côté','encre','s')
save(fig,'47-065')
