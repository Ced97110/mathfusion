import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
text(ax,44,43,'aucune règle pour comparer','fixe','s')
R={'x':'sujet','y':'autre'}
for x0,w in ((10,'xy'),(61,'yx')):
    for i,ch in enumerate(w):
        box(ax,x0+i*9.5,24,9,9,R[ch],label='$%s$'%ch,size='l')
    brace(ax,x0,x0+18.5,22,'fixe',label='$%s$'%w)
text(ax,44,29,r'$\neq$','encre','xl')
text(ax,44,5,'deux éléments différents','encre','s')
save(fig,'49-005')
