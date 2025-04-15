# CORDEX-FPSCONV Simulation Protocol

## Terms of use

The ensemble of convection-permitting simulations is only accessible to consortium members until the data is made public via ESGF (target end of 2021).
Please read and follow the [Terms of Use](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_terms_of_use.pdf).
Contact Erika and Stefan with any questions.

## Domain

In this document the rotated and other system coordinates are reported for the FPS mandatory domain.

[Download domain file](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_mandatory_model_domain_v02_20161206.pdf)

## Settings

- No nudging
- Common model systems coordinate their set-ups (e.g. common grid, sponge layer, vertical levels, soil moisture spin-up, etc.)
- Shallow convection turned on (suggested, not mandatory)
- Soil moisture: each model system uses its own spin-up procedure
- Lake model turned on (if available)
- Vertical levels: up to modeling teams but 35–50+ recommended
- LBC update frequency up to model groups
- SST from ERA-Interim (some groups may want to do sensitivity tests with higher resolution)
- Model top: up to modeling teams, the higher the better (~20 hPa)
- Nesting strategy: Directly from ERA-Interim or from the 0.11 Euro/Med/Coupled-Med CORDEX domains

## Experiments

- Three case studies
- ERA-Interim evaluation run 2000–2014 (if possible), minimum 10 years
- Aim for groups to have 1 year of evaluation run (1999) done by June 2017
- Tentative CMIP5 simulation time slices:
  1. HIST: 1996–2005  
  2. RCP8.5: 2041–2050  
  3. RCP8.5: 2090–2099

## Variable List and Documentation

updates to `mrsol` 16.03.2021 (see example for how to define `soil_layer` below)

```
double soil_layer(soil_layer) ;
  soil_layer:standard_name = "depth" ;
  soil_layer:long_name = "Soil layer depth" ;
  soil_layer:units = "m" ;
  soil_layer:positive = "down" ;
  soil_layer:axis = "Z" ;
  soil_layer:bounds = "soil_layer_bnds" ;

double soil_layer_bnds(soil_layer, bnds) ;

float mrsol(time, soil_layer, y, x) ;
  mrsol:standard_name = "moisture_content_of_soil_layer" ;
  mrsol:long_name = "Total water content of soil layer" ;
  mrsol:units = "kg m-2" ;
  mrsol:grid_mapping = "crs" ;
  mrsol:coordinates = "lat lon" ;
  mrsol:_FillValue = 1.e+20f ;
  mrsol:missing_value = 1.e+20f ;
  mrsol:cell_methods = "time: mean" ;
```

[fps_convection_variables_vfinal_2021update.xlsx](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_variables_vfinal_2021update.xlsx)

## Filenaming Convention

The file below gives the filenaming convention.
This was chosen in order to meet the requirements of the ESGF.
First file was up-to-date as of 30.09.2019.
After the Toulouse annual meeting (11.2019) some minor changes were agreed and further testing has been performed. 
Therefore, an updated document appears below along with an example `ncdump.txt` file that shows what the netcdf metadata and attributes should look like.
In the document some lingering issues related to the QA-checker and ESGF are noted and will be solved in collaboration with DKRZ (29.10.2020).

- [fps_convection_filenanaming.pdf](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_filenanaming.pdf)
- [fps_convection_filenanaming_2020_update.pdf](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_filenanaming_2020_update.pdf)
- [ncdump_pr.pdf](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=ncdump_pr.pdf)

The documents below are important and relevant for a compliant CMORization of the FPS output data.
The variable list above follows these requirements but differs in ways that are unique to the FPS such as output frequency and type of variables in "CORE" and "Tier-1", etc.
Use these as a guide and ask the consortium for help via the email list if anything is unclear.

- [cordex_archive_specifications.pdf](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=cordex_archive_specifications.pdf)
- [cordex_variables_requirements_table_140221.pdf](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=cordex_variables_requirements_table_140221.pdf)

## Remapping Toolbox

In case teams wish to remap to a common 3km grid (ALP3i) a common toolbox should be used.
Initially developed by Erik van Meijgaard and improved Hans-Jeurgen Panitz, you can download the tarball below.

[eur_cordex_remapping_tool.tar](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=eur_cordex_remapping_tool.tar)

## Test Case Selection Results

[doodle-results-case-studies.xls](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=doodle-results-case-studies.xls)

## Test Cases Protocol as decided after the 10th HyMeX Workshop in Barcelona

 1. For each of the test cases ERA-interim will be used as BC and the 0.11 as intermediate resolution (EURO/Med-CORDEX domain) to get to the resolution of the mandatory domain.
 2. For each of the test cases the weather like (WL) simulation and the climate mode (CM) simulation will be
initialized in the same way for both the 0.11 and the high resolution (3km) domains.
 3. The suggested initialization procedure for the test cases is the following:
    * Case 1 - IOP16 (23-28 October 2012): INIT-WL:2012102300-END:2012102800 INIT-CM:2012100100-END:2012110100
    * Case 2 - AUSTRIA (20-27 June 2009): INIT-WL:2009062000-END:2009062700 INIT-CM:2009060100-END:2009070100
    * Case 3 - FOEHN (2-7 November 2014): INIT-WL:2014110200-END:2014110700 INIT-CM:2014100100-END:2014110700

## Case 1: Observations

Regridded stations data on a regular 0.05 deg grid are available here:

[geo_v3_gridded_0.05.nc.gz](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=geo_v3_gridded_0.05.nc.gz)

---
*Document last modified: 2021/03/16 12:26 by Stefan. Source: [Original wiki page](https://www.hymex.org/cordexfps-convection/wiki/doku.php?id=protocol)*

Cite as: CORDEX-FPSCONV (2025) _CORDEX-FPSCONV simulation protocol_. Zenodo. https://doi.org/10.5281/zenodo.14960532
