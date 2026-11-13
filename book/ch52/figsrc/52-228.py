import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
for r in range(5):
    for c in range(5):
        box(ax,4+c*6,22+r*6,5,5,'sujet',lw=0.5,r=0.5)
        box(ax,55+c*6,22+r*6,5,5,'resultat',lw=0.5,r=0.5)
text(ax,18.5,56,r'25 facteurs $7^{4}$','sujet','s')
text(ax,69.5,56,'25 facteurs égaux à 1','resultat','s')
arrow(ax,(36,36.5),(52,36.5),'varie'); text(ax,44,41,r'$7^{4}\equiv1$','varie','s')
text(ax,44,10,r'$7^{100}=(7^{4})^{25}\equiv1^{25}=1$','encre','m')
save(fig,'52-228')
