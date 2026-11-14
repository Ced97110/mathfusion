import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
rows=[r'1. $a=1,\ b=-6,\ c=9$', r'2. $D=36-36=0$', r'3. $\sqrt{D}$ remplacé par 0', r'4. $x=(6\pm0)/2$', r'5. diviser par 2 : $x=3$']
for i,s in enumerate(rows):
    y=62-i*14
    role='resultat' if i==4 else 'sujet'
    box(ax,2,y,44,9,role,True,s,size='s')
    if i<4: arrow(ax,(24,y),(24,y-4.2),'fixe')
box(ax,52,20,14,9,'varie',True,'6'); box(ax,68,20,14,9,'varie',True,'6')
arrow(ax,(46,24.5),(51.2,24.5),'varie')
box(ax,50,6,36,9,'autre',True,r'$x=-b/(2a)$',size='s')
arrow(ax,(46,10.5),(49.2,10.5),'autre')
text(ax,67,17.8,'lettres, sans racine','autre','s')
save(fig,'23-068')
