#!/bin/bash
#Using just protein doesnt seem to make a difference to output but is significantly faster:

sys=("pkG" "pkA" "pkL" "pkkg" "pkka" "pkkl")

calc_com(){

	for i in 0 1 2 3 4 5;do
        	echo "${sys[i]}:pwd:`pwd`"

        	#top="/media/taniaraj/DATA/single_systems/gen*/${sys[i]}/step2/no_water/nowater.psf"
        	#traj="/media/taniaraj/DATA/single_systems/gen*/${sys[i]}/step2/no_water/nowater.nc"
		
		top="../../gen*/${sys[i]}/step2/centered/step3_input.psf"
		traj="../../gen*/${sys[i]}/step2/centered/center.nc"
		
		if [ -f "$traj" ]; then

			vmd -dispdev text -psf $top -netcdf $traj -e com_dist.tcl
			mv com_dist.out ${i}_com.out
		else
			top="../../gen*/${sys[i]}/step2/centered/step3_input.psf"
                	traj="../../gen*/${sys[i]}/step2/centered/center1.nc"
			vmd -dispdev text -psf $top -netcdf $traj -e com_dist.tcl
			mv com_dist.out ${i}_com1.out

			top="../../gen*/${sys[i]}/step2/centered/step3_input_2.psf"
			traj="../../gen*/${sys[i]}/step2/centered/center2.nc"
			vmd -dispdev text -psf $top -netcdf $traj -e com_dist.tcl
                        mv com_dist.out ${i}_com2.out
		fi

	done
}
calc_com
