# MTP Info

## Training Cycle

### Train

#### Input Files

`curr.mtp`
`train.cfg`

#### Output Files

`None`

#### mlp Command

`mlp train curr.mtp train.cfg --max-iter=500 --trained-opt-name=curr.mtp --curr-pot-name=curr.mtp --stress-weight=5e-4 --force-weight=5e-3`

#### Purpose

Trains the potential in `curr.mtp` on the data in `train.cfg`. [GLWH Nov 26 2020] In other words, this is the _fit_. This is the part a potential is fitted to the energies, forces, and stresses in a group of vasp calculations. 

### Calc Grade

#### Input Files

`curr.mtp`
`train.cfg`
`train.cfg`
`temp.cfg`

#### Output Files

`temp.cfg`
`state.als`

#### mlp Command

`mlp calc-grade curr.mtp train.cfg train.cfg temp.cfg --nbh-weight=0.0 --energy-weight=1.0`

#### Purpose

Calculates the MV Grade of `train.cfg` and sets up the `state.als` file. [GLWH Nov 26 2020] The MV grade isn't needed. But the `als` file stores the active learning set.

### Relax

#### Input Files

`mlip.ini`
`curr.mtp`
`catalog.cfg`

#### Output Files

`relaxed.cfg_*`
`unrelaxed.cfg_*`
`selected.cfg_*`

Note: The `_*` signifies that there will probably be multiple files, depending on the number of processes you are running the command with.  
[GLWH Nov 26 2020]  
For me the output files are B-*pre*selected.cfg_#. And watch out! If you run this command twice in a row, without deleting `B-preselected.cfg` it *appends* to the file. Gotcha!


#### mlp Command

`mlp relax mlip.ini --force-tolerance=1e-3 --stress-tolerace=1e-2 --max-step=0.03 --cfg-filename=catalog.cfg --save-relaxed=relaxed.cfg --save-unrelaxed=unrelaxed.cfg`

#### Purpose

This is sort of the heart of the MTP algorithm. It attempts to relax the structures in `catalog.cfg` to an equilibrium state.
If it fails to do so,  within a certain tolerance of estimated error, the structures that break this tolerance are collected. [GLWH Nov 26 2020] Some (or all of these _preselected_ structures will be added to the training set. This selection is done in the next step: select-add.

### Select Add


#### Input Files

`curr.mtp`
`train.cfg`
`selected.cfg`
 `state.als`

Note: `selected.cfg` is a concatenation of all `selected.cfg_*` from the previous step

#### Output Files

`diff.cfg`
`active_set.cfg`

#### mlp Command

`mlp select-add curr.mtp train.cfg selected.cfg diff.cfg --select-threshold=3.0 --nbh-weight=0.0 --energy-weight=1.0 --als-filename=state.als --selected-filename=active_set.cfg`

#### Purpose

This step selects files from `selected.cfg` to run in VASP. These will then be added to the training set and the process starts again. 

## Errors Encountered when Training MTP's

### Potential mlp Errors:

#### `train` Step Hangs Forever

"This often happens when there are too few configurations in the database - there is a condition that the error on each iteration should decrease, but when there are too little configurations, severe overfitting occurs and the iterative algorithm cannot decrease the error due to round-off errors. Can be safely ignored and forgotten about when you expand the training database sufficiently large. Not easy to detect automatically, though." - Alexander Shapeev

#### MLIP: ERROR: Error reading .* file

This error occurs when you have an input in an `mlp` command but the file it refers to is not there. For example, if you see `MLIP: ERROR: Error reading .mtp file`, then your mtp file is missing.

### Potential AutoGR Errors:

It is especially important to look out for AutoGR errors because if AutoGR fails, VASP will automatically generate KPOINTS for you, and most likely not at the same KPOINT density you want.

#### The point group doesn't match the niggli basis id

This one hopefully will be fixed soon in the AutoGR code.

### Potential VASP Errors:

#### Internal error in subroutine SGRCON: Found some non-integer element in rotation matrix

This has an unknown cause, but could be caused by ... (maybe add some more info here that I don't know).
