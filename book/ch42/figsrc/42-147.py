import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
data=[('A','sujet',['1','2']),('B','autre',['2','3']),('C','fixe',['2','4'])]
for i,(l,r,els) in enumerate(data):
    x=3+i*28.5; box(ax,x,36,25,14,r); text(ax,x+12.5,55,l,r,'l')
    for j,e in enumerate(els): disc(ax,x+7+j*11,43,3,'resultat' if e=='2' else r,label=e)
brace(ax,3,85,33,'fixe')
text(ax,44,24,'seul le 2 est dans les trois','resultat','s')
box(ax,2,5,41,9,'resultat',label=r'$(A\cap B)\cap C=\{2\}$',size='s')
box(ax,45,5,41,9,'resultat',label=r'$A\cap(B\cap C)=\{2\}$',size='s')
save(fig,'42-147')
