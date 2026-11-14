import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,2,46,'phrase complète','fixe','m',ha='left'); text(ax,2,24,'avec la convention','fixe','m',ha='left')
box(ax,2,31,38,9,'sujet',label=r'$x^2-2$ est premier',size='m'); box(ax,43,31,43,9,'fixe',label='coefficients entiers',size='s')
box(ax,2,9,38,9,'sujet',label=r'$x^2-2$ est premier',size='m'); box(ax,43,9,43,9,'fixe',fill=False,dash=True,label='sous-entendu',size='s')
text(ax,63,4,'même sens, écrit plus court','resultat','s')
save(fig,'18-103')
