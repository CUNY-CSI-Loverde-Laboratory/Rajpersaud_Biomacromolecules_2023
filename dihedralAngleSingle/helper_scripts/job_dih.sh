#!/bin/bash

<<STEP1
pep="pkG"
top="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/original_trajs/run2.nc"
        
conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep
        
pep="pkA"
top="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/original_trajs/run2.nc"
        
conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep

pep="pkL"
top="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen1/$pep/step2/original_trajs/run2.nc"

conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep

pep="pkkg"
top="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/run6.nc"

conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep

pep="pkka"
top="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/run6.nc"

conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep

pep="pkkl"
top="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/step3_input.psf"
traj="/media/taniaraj/DATA/single_systems/gen2/$pep/step2/AMBER/charmm-gui-2/amber/run6.nc"

conda activate AmberTools22
cpptraj -p $top -y $traj -i dihedral.in 2>&1 | tee dihedral.log;
conda deactivate

mkdir $pep
mv *.dat $pep
mv *.hist $pep

STEP1

#<<STEP2
sys=("pkG" "pkA" "pkL" "pkkg" "pkka" "pkkl")
peptides=("A" "B")

#for i in 0 1 2 3 4 5;do
#        echo "${sys[i]}:pwd:`pwd`"
#	for p in ${peptides[@]};
#        do
#                echo "Generating csv file for ${sys[i]} $p ..."
#                python3 to_csv.py ${sys[i]}/dihedral_$p.dat dihedral_${p}_${sys[i]}.csv
#                echo "Done with ${sys[i]} $p ..."
#        done
#done
#STEP2

for i in 0 1 2 3 4 5;do
        echo "${sys[i]}:pwd:`pwd`"
        for p in ${peptides[@]};
        do
        	#echo "$s$p"
		#fr=`tail -n1 ${sys[i]}/dihedral_A.dat | awk '{print $1}'` #get last frame number
                echo "Generating pair file for ${sys[i]} $p ..."
                
		python3 to_pairs.py ${sys[i]}/dihedral_$p.dat ${i}_${p}_${sys[i]}.csv $fr || error_exit
                echo "Done with ${sys[i]} $p ..."
	done
done
