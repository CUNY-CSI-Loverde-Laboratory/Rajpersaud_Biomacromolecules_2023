## MAIN_PROC_
set total [molinfo top get numframes]
  
# select chain a and chain b separately
set chaina [atomselect top "segname PROA"]
set chainb [atomselect top "segname PROB"]

set last [expr $total-1]
set molid 0
set vec1 [veczero]
set vec2 [veczero]

set outFile [open "com_dist.out" w]

for {set i 0} {$i<=$last} {incr i} {
	$chaina frame $i
	$chaina update

	$chainb frame $i
        $chainb update

	set vec1 [measure center $chaina weight mass]
        set vec2 [measure center $chainb weight mass]
	
	set vec1 [veclength [vecsub $vec1 $vec2]]
	
	puts $outFile "frame $i: $vec1"
}

close $outFile
exit

