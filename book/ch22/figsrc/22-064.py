import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
L=[(r'$16+9$','sujet'),('25','sujet'),('5','sujet')]; R=[(r'$\sqrt{16},\ \sqrt{9}$','autre'),(r'$4$ et $3$','autre'),('7','autre')]
for i in range(3):
    y=44-i*20
    box(ax,5,y,34,11,role=L[i][1],label=L[i][0]); box(ax,49,y,34,11,role=R[i][1],label=R[i][0])
for x in (22,66):
    arrow(ax,(x,44),(x,36),'varie'); arrow(ax,(x,24),(x,16),'varie')
text(ax,24.5,40,'additionner','varie','s',ha='left'); text(ax,24.5,20,'racine','varie','s',ha='left')
text(ax,68.5,40,'racines','varie','s',ha='left'); text(ax,68.5,20,'additionner','varie','s',ha='left')
text(ax,44,17.5,r'$\neq$','limite','l')
save(fig,'22-064')
