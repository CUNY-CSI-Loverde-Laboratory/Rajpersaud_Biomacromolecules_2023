#!/bin/bash

sys=("pkG" "pkA" "pkL" "pkkg" "pkka" "pkkl")
 
for i in 0 1 2 3 4 5;do
   echo "Generating ss matrix file for ${sys[i]}..."
   #cd ${sys[i]}
   fr=`tail -n1 dssp_${sys[i]}.gnu | awk '{print $1}'`
   fr=`echo "$fr-2" | bc`
   python3 secStruct.py $fr "dssp_${sys[i]}.gnu"
   #cd ..
   echo "Done with ${sys[i]} $p ..."
   mv secstruct_frac.txt ${sys[i]}_ss_frac.txt
   mv secstruct_count.txt ${sys[i]}_ss_count.txt
done
