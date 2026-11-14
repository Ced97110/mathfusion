import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,4,56,80,11,'fixe',label=r'$a\leq b$ quand $a\vee b=b$')
arrow(ax,(44,55),(44,46),'varie'); text(ax,49,50.5,'a devient O, b devient a','varie','s',ha='left')
box(ax,4,34,44,11,'sujet',label=r'$O\vee a=a$'); text(ax,52,39.5,'vrai par A4','resultat','s',ha='left')
arrow(ax,(26,33),(26,25),'varie'); text(ax,31,29,'donc','varie','s',ha='left')
box(ax,4,13,44,11,'resultat',label=r'$O\leq a$'); text(ax,52,18.5,'O est sous tout a','resultat','s',ha='left')
save(fig,'80-154')
