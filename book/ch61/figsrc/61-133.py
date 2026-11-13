import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,2,2,84,72,'fixe')
text(ax,44,69,r'$E$','fixe','s')
box(ax,8,8,72,54,'sujet')
text(ax,44,57,r'clôture de $F$ dans $E$','sujet','s')
box(ax,16,14,36,26,'resultat'); text(ax,34,35,r'$F$','resultat','m')
text(ax,66,26,r'$\sqrt{2}$','sujet','s')
disc(ax,66,36,0.01,'sujet') if False else None
text(ax,15,3.6,r'$\pi$ : hors de la clôture','limite','s') if False else None
text(ax,70,66,r'$\pi$','limite','s')
text(ax,40,24,r'$F=\mathbb{Q}$','resultat','s') if False else None
text(ax,44,45,r'$F=\mathbb{Q},\ E=\mathbb{C}$','fixe','s') if False else None
save(fig,'61-133')
