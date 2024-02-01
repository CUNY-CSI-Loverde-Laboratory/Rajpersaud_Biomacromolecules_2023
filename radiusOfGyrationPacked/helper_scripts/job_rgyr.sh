#!/bin/bash
#Using just protein doesnt seem to make a difference to output but is significantly faster:

sys=("pkG_peG" "pkA_peA" "pkL_peL" "pkkg_peeg" "pkka_peea" "pkkl_peel")
strands=("OA" "OB" "OC" "OD" "OE" "OF" "OG" "OH" "OI" "OJ" "OK" "OL" "OM" "ON" "OO" "OP" "OQ" "OR" "OS" "OT" "OU" "OV" "OW" "OX" "OY" "OZ" "AA" "AB" "AC" "AD" "AE" "AF" "AG" "AH" "AI" "AJ" "AK" "AL" "AM" "AN")

calc_rgyr_packed () {
	for i in 0 1 2 3 4 5;do
		echo "${sys[i]}:pwd:`pwd`"
		top="step3_input_noWater.pdb"
        	traj="gromacs/no_water/*.xtc"
		vmd -dispdev text -pdb ${top} -xtc ${traj} -e rgyr.tcl
		echo exit
        	mkdir ${sys[i]}
        	mv *.out ${sys[i]}
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

#calc_rgyr_packed
merge_files
