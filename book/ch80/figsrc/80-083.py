import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(56)
text(ax,44,50,'ℤ/2, dimension 3 : 8 vecteurs','encre','m')
codes=['000','100','010','001','110','101','011','111']
for i,c in enumerate(codes):
    box(ax,2.75+i*10.5,30,9,9,'fixe' if i==0 else 'sujet',label=c,size='s')
text(ax,7.25,24,'nul','fixe','s')
brace(ax,13.25,85.25-1.5,29,'resultat',label='7 non nuls : 7 points')
save(fig,'80-083')
