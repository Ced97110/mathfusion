import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,22,62,'on part de','encre','m'); text(ax,70,62,'on arrive à','encre','m')
box(ax,4,36,36,10,'sujet',label='26 ≡ 2',size='l'); box(ax,4,20,36,10,'autre',label='27 ≡ 3',size='l')
box(ax,54,44,32,9,'fixe',label='26 × 27 = 702'); box(ax,54,31,32,9,'fixe',label='2 × 3 = 6')
arrow(ax,(41,41),(53,48.5),'varie',lw=1.4); arrow(ax,(41,25),(53,35.5),'varie',lw=1.4)
arrow(ax,(70,30),(70,25),'varie')
box(ax,54,14,32,11,'resultat',label='702 ≡ 6',size='l'); text(ax,70,8,'696 = 58 × 12','resultat','m')
save(fig,'47-101')
