#!/bin/bash

sys=("pkG_peG" "pkA_peA" "pkL_peL" "pkkg_peeg" "pkka_peea" "pkkl_peel")

calc_PCA () {
	for i in 0 1 2 3 4 5;do
		echo "${sys[i]}:pwd:`pwd`"
		top1="gromacs/single_peps/*_neg.pdb"
		top2="gromacs/single_peps/*_pos.pdb"

		traj1="gromacs/single_peps/neg_last_900ns.xtc"
		traj2="gromacs/single_peps/pos_last_900ns.xtc"

		python3 PCA.py $top1 $traj1 "neg"
		python3 PCA.py $top2 $traj2 "pos"

		mkdir ${sys[i]}
		mv *.csv ${sys[i]}
		mv pc*.xtc ${sys[i]}
		mv pc*.gro ${sys[i]}
	done
}
plot_PCA(){
	for i in 0;do
		cd ${sys[i]}
		echo `pwd`
		python3 ../PCA_plot.py all_PCA_neg.csv ${sys[i]} 
		python3 ../PCA_plot.py all_PCA_pos.csv ${sys[i]}
		cd ..
	done
}

#calc_PCA
plot_PCA
