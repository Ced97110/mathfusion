import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,65,'$x=36°$','encre','m')
box(ax,3,15,37,34,'sujet'); box(ax,48,15,37,34,'autre')
text(ax,21.5,54,'sin 11x + sin 10x','sujet','s'); text(ax,66.5,54,'2 sin(21x/2) cos(x/2)','autre','s')
text(ax,44,32,'=','resultat','xl',weight='bold')
for i,t in enumerate(('sin 396° = 0,5878','sin 360° = 0','0,5878 + 0','= 0,5878')):
    text(ax,21.5,43-7*i,t,'sujet','s',weight='bold' if i==3 else 'normal')
for i,t in enumerate(('sin 378° = 0,3090','cos 18° = 0,9511','2 × 0,3090 × 0,9511','= 0,5878')):
    text(ax,66.5,43-7*i,t,'autre','s',weight='bold' if i==3 else 'normal')
save(fig,'35-092')
