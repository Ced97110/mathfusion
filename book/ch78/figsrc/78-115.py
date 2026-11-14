import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,16,48,r'$\mathbb{H}$','sujet',26,weight='bold')
text(ax,16,38,'quaternions','sujet','m')
text(ax,16,33,'de Hamilton','sujet','m')
for i,(lab,role) in enumerate([('réel','fixe'),(r'$\times i$','sujet'),(r'$\times j$','sujet'),(r'$\times k$','sujet')]):
    box(ax,36+(i%2)*25,50-(i//2)*13,23,11,role,label=lab)
text(ax,59,28,'4 coordonnées','sujet','m')
line(ax,[(2,22),(86,22)],'fixe',dash=True)
text(ax,15,12,'même écriture :','fixe','s')
for x,l,r in [(40,r'$\mathbb{R}$','fixe'),(55,r'$\mathbb{C}$','autre'),(70,r'$\mathbb{H}$','sujet')]:
    text(ax,x,12,l,r,'l',weight='bold')
save(fig,'78-115')
