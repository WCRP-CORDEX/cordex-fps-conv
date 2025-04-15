# CORDEX-FPSCONV Simulation Protocol

## Terms of use

**Note:** The ensemble of convection-permitting simulations is only accessible to consortium members until the data is made public via ESGF (target end of 2021). Please read and follow the [Terms of Use](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_terms_of_use.pdf). Contact Erika and Stefan with any questions.

---

## Domain

Rotated and other system coordinates are reported for the FPS mandatory domain.

[Download domain file](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_mandatory_model_domain_v02_20161206.pdf)

---

## Settings

- No nudging
- Common model systems coordinate their set-ups:
  - Common grid
  - Sponge layer
  - Vertical levels
  - Soil moisture spin-up
- Shallow convection: **suggested**, not mandatory
- Soil moisture: each model system uses its own spin-up procedure
- Lake model: turned on (if available)
- Vertical levels: 35–50+ recommended
- LBC update frequency: up to model groups
- SST: from ERA-Interim (optionally test higher resolution)
- Model top: up to modeling teams (the higher, the better — ~20 hPa)
- Nesting strategy:
  - Directly from ERA-Interim
  - Or from 0.11 Euro/Med/Coupled-Med CORDEX domains

---

## Experiments

- **Three case studies**
- **ERA-Interim evaluation run:** 2000–2014 (if possible), minimum 10 years
  - Aim: have 1 year (1999) done by June 2017

**CMIP5 Simulation Time Slices:**

1. HIST: 1996–2005  
2. RCP8.5: 2041–2050  
3. RCP8.5: 2090–2099

---

## Variable List and Documentation

Updated `mrsol` variable on 16.03.2021.

Example of how to define `soil_layer`:

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

[Variable definitions spreadsheet](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_variables_vfinal_2021update.xlsx)

---

## Filenaming Convention

- Original file (as of 30.09.2019)
- Updates after the Toulouse annual meeting (11.2019)
- Notes on QA-checker and ESGF issues

Documents:
- [Original filenaming PDF](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_filenanaming.pdf)
- [2020 update](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=fps_convection_filenanaming_2020_update.pdf)
- [ncdump example](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=ncdump_pr.pdf)

Other references:
- [CORDEX archive specifications](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=cordex_archive_specifications.pdf)
- [CORDEX variable requirements (Feb 2021)](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=cordex_variables_requirements_table_140221.pdf)

---

## Remapping Toolbox

- For remapping to a common 3km grid (ALP3i)
- Toolbox by Erik van Meijgaard, improved by Hans-Jürgen Panitz

[Download remapping tool](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=eur_cordex_remapping_tool.tar)

---

## Test Case Selection Results

[Selection results (doodle)](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=doodle-results-case-studies.xls)

---

## Test Case Protocol (from 10th HyMeX Workshop, Barcelona)

**For each test case:**
- ERA-Interim used as BC
- 0.11 resolution (EURO/Med-CORDEX domain) down to mandatory domain resolution
- Both WL (weather-like) and CM (climate mode) simulations initialized the same way

### Initialization Procedures

- **Case 1 – IOP16 (23–28 October 2012):**  
  - `INIT-WL: 2012102300 – END: 2012102800`  
  - `INIT-CM: 2012100100 – END: 2012110100`  

- **Case 2 – AUSTRIA (20–27 June 2009):**  
  - `INIT-WL: 2009062000 – END: 2009062700`  
  - `INIT-CM: 2009060100 – END: 2009070100`  

- **Case 3 – FOEHN (2–7 November 2014):**  
  - `INIT-WL: 2014110200 – END: 2014110700`  
  - `INIT-CM: 2014100100 – END: 2014110700`  

---

## Case 1 Observations

Regridded station data on a regular 0.05° grid:

[Download observation file (geo_v3_gridded_0.05.nc.gz)](https://www.hymex.org/cordexfps-convection/wiki/lib/exe/fetch.php?media=geo_v3_gridded_0.05.nc.gz)

---

*Document last modified: 2021/03/16 12:26 by Stefan*

Source:  
[Original wiki page](https://www.hymex.org/cordexfps-convection/wiki/doku.php?id=protocol)
