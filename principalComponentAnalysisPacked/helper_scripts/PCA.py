#!/usr/bin/env python3

import MDAnalysis as mda
from MDAnalysis.analysis import pca, align
import numpy as np
import pandas as pd
import sys

## Command-Line arguements ##

top = sys.argv[1]   # Topology file: top ="pkkl_neg.pdb"
traj = sys.argv[2]  # Trajectory file: traj = "pep22.xtc"
nm = sys.argv[3]    # Output file names

print("Creating universe...")
u = mda.Universe(top, traj)

## PCA data generation ##

print("Starting PCA...")
# select='backbone' doesnt work for uncommon proteins (ie D-chiral residues)
aligner = align.AlignTraj(u, u, select='name CA or name C or name N', in_memory=True).run()
pc = pca.PCA(u, select='name CA or name C or name N', align=True, mean=None, n_components=None).run()

## Checking analysis ##

backbone = u.select_atoms('name CA or name C or name N')
n_bb = len(backbone)
print('There are {} backbone atoms in the analysis'.format(n_bb))
print('PC shape:', pc.p_components.shape)
n_pcs = np.where(pc.cumulated_variance > 0.95)[0][0]
print("The number of PC's needed to explain 95% of the variance is:",n_pcs)

## Write out PC1 and PC2 as CSV files ##

print("Creating csv file for PC1 and PC2")
transformed = pc.transform(backbone, n_components=2)
df = pd.DataFrame( transformed, columns=['PC{}'.format(i+1) for i in range(2)] )
df['Time (ps)'] = df.index * u.trajectory.dt
df.to_csv('all_PCA_' + nm + '.csv')

# Project coodinates onto PC1 ("extracting movements") ##

print("Extracting movements over PC1")
#pc1 = pc.p_components[:, 0]
#trans1 = transformed[:, 0]
#projected = np.outer(trans1, pc1) + pc.mean.flatten()
#coordinates = projected.reshape(len(trans1), -1, 3)
projected = pc.project_single_frame(components=[0,1])
u.trajectory.add_transformations(projected)
#coordinates = projected.reshape(len(trans1), -1, 3)

#proj1 = mda.Merge(backbone) # create new universe with backbone atom group
#proj1.load_new(coordinates, order="fac") #load new trajectory into universe

protein = u.select_atoms("name CA or name C or name N")
with mda.Writer("pc_"+nm+".xtc", protein.n_atoms) as W:
    for ts in u.trajectory:
        W.write(protein)

# Write out GRO FILE
protein.atoms.write('pc_'+nm+'.gro',reindex=False)
