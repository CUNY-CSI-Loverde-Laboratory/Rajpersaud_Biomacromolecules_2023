#!/bin/bash
#Using just protein doesnt seem to make a difference to output but is significantly faster:

sys=("pkG_peG" "pkA_peA" "pkL_peL" "pkkg_peeg" "pkka_peea" "pkkl_peel")

calc_hbond () {
	for i in 0 1 2 3 4 5;do
		echo "${sys[i]}:pwd:`pwd`"
		top="gromacs/no_water/step3_input_noWater.pdb"
        	traj="gromacs/no_water/*.xtc"
	
		conda activate AmberTools22
       	 	cpptraj -p $top -y $traj -i intra.in &>> intra.log;
        	cpptraj -p $top -y $traj -i inter.in &>> inter.log
        	conda deactivate

       	 	mkdir ${sys[i]}
        	mv *.dat ${sys[i]}
        	mv *.gnu ${sys[i]}

        	## Sum together all the intra values for each peptide:
        	cd ${sys[i]}
        	echo "${sys[i]}:pwd:`pwd`"
        	fr=`tail -n1 intraOA.dat | awk '{print $1}'`
        	python3 ../count_intra_all.py ${sys[i]} $fr
        	cd ..	
	done
}
merge_files () {
	for i in 0 1 2 3 4 5;do
		cd ${sys[i]}
		echo "${sys[i]}..."
		for j in ${strands[@]};do
			awk '{print $4}' rgyr_PR${j}.out > tmp_$j
		done
		paste tmp* > rgyr_ALL.out
		rm tmp*
		cd ..
	done	
}

calc_hbond
#merge_files
