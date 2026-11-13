import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i in range(3):
    y=50-12*i
    text(ax,31,y+4.5,f'lettre {i+1}','fixe','s',ha='right')
    for j in range(3):
        one=(i==j); box(ax,34+10*j,y,9,9,'sujet' if one else 'fixe',label='1' if one else '0')
text(ax,48,19,'un seul 1, les autres 0','fixe','s')
text(ax,44,9,r'$(0,\ldots,1,\ldots,0)$','sujet','l')
save(fig,'49-059')
