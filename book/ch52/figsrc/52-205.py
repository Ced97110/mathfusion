import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,54,'somme de 1, répétée','encre','m')
text(ax,4,44,'ℤ, ℚ, ℝ : k = 0','sujet','s',ha='left')
for i,l in enumerate(['1','2','3','4','…']):
    box(ax,4+i*11,32,9,8,'sujet',label=l,size='s')
    if i<4: arrow(ax,(13+i*11,36),(15+i*11,36),'varie',lw=0.8)
arrow(ax,(59,36),(80,36),'varie')
text(ax,84,36,'','encre')
text(ax,4,22,'ℤ/6ℤ : k = 6','autre','s',ha='left')
for i,l in enumerate(['1','2','3','4','5','0']):
    box(ax,4+i*11,8,9,8,'resultat' if l=='0' else 'autre',label=l,size='s')
    if i<5: arrow(ax,(13+i*11,12),(15+i*11,12),'varie',lw=0.8)
save(fig,'52-205')
