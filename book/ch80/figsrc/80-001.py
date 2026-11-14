import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
rows=[('Les nombres','compter les entiers de 1 à 30\nsans facteur commun avec 30'),
      ('Les droites','un système de deux équations\nsans solution'),
      ('L’électricité','simplifier un montage\nde six interrupteurs')]
for i,(a,b) in enumerate(rows):
    y=50-i*19
    box(ax,2,y,24,14,'fixe',label=a,size='s')
    box(ax,30,y,56,14,'sujet',label=b,size='s')
    if i<2: text(ax,14,y-2.5,'?','limite','m')
text(ax,44,5,'trois exercices, aucun rapport apparent','encre','s')
save(fig,'80-001')
