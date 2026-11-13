import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'les 5 égalités de la chaîne','encre','m')
for i in range(5):
    r='varie' if i%2==0 else 'fixe'
    disc(ax,12+i*16,46,5.5,r,label=str(i+1),size='l')
box(ax,4,18,40,10,'varie',label='parenthèse déplacée')
box(ax,48,18,36,10,'fixe',label='signe changé')
text(ax,24,10,'1, 3 et 5 : associativité','varie','s'); text(ax,66,10,'2 et 4 : règle de signe','fixe','s')
save(fig,'78-156')
