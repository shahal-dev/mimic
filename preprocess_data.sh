cd ./data
conda activate ciao
rm -rf ./parent/reprocessed_data/16626
chandra_repro 16626 verbose=1 outdir = .././parent/Ophiuchus/reprocessed_data/16626 clobber = yes
punlearn ardlib
rm -rf ./parent/reprocessed_data/16627
chandra_repro 16627 verbose=1 outdir = .././parent/Ophiuchus/reprocessed_data/16627 clobber = yes
punlearn ardlib
rm -rf ./parent/reprocessed_data/16464
chandra_repro 16464 verbose=1 outdir = .././parent/Ophiuchus/reprocessed_data/16464 clobber = yes
punlearn ardlib
rm -rf ./parent/reprocessed_data/16142
chandra_repro 16142 verbose=1 outdir = .././parent/Ophiuchus/reprocessed_data/16142 clobber = yes
punlearn ardlib
rm -rf ./parent/reprocessed_data/16143
chandra_repro 16143 verbose=1 outdir = .././parent/Ophiuchus/reprocessed_data/16143 clobber = yes
punlearn ardlib
