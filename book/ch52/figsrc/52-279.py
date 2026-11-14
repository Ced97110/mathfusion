import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
o=22
text(ax,44,47+o+4,r'$M_2(\mathbb{R})$ : deux idéaux seulement','sujet','m')
text(ax,44,47+o-3,r'$\{0\}$ et $M_2(\mathbb{R})$','sujet','m')
def grid(x0,role,labs):
    for k,l in enumerate(labs):
        box(ax,x0+(k%2)*8,26+o-(k//2)*8,8,8,role if l!='0' else 'fixe',label=l,size='s')
grid(8,'sujet',['1','0','0','0'])
text(ax,30,26+o,r'$\times$','encre','l')
box(ax,36,18+o,16,16,'autre',label=r'$B$ quelconque',size='s')
text(ax,58,26+o,'=','encre','l')
grid(64,'varie',['a','b','0','0'])
text(ax,16,9+o,r'$A\neq0$','sujet','s')
text(ax,70,9+o,'ligne 2 nulle','fixe','s')
text(ax,44,22,"jamais l'unité : A sans inverse",'varie','s')
text(ax,44,12,"donc pas un corps :",'encre','s')
text(ax,44,5.5,"« commutatif » est nécessaire",'encre','s')
save(fig,'52-279')
