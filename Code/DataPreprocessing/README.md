# Data Preprocessing

Run items in this folder to move on to drought analysis.

### Requirements:
 - Must download data from ADWR GIS database: https://gisdata2016-11-18t150447874z-azwater.opendata.arcgis.com/
    - Well_Registry
    - GWSI_App
 - Need the latest GRACE data:
 https://www2.csr.utexas.edu/grace/RL0602_mascons.html
 - Move these files into the Data/Input folder.
 - Download "georeg_reproject_fixed" files from here:
 https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/Tadych_AzGroundwaterSpatialAnalysis_Aug2023/Data/Shapefiles
 - Place in Data/Input/Shapefiles folder.

 ### Run Codes
 1. First, need to merge the well databases
    - Run 1_WellStaticMerge.py
    - Run 1_WellTSMerge.py
 2. Second, run spatial analysis scripts
    - Run 2_SpatialAnalysisGrace.py
    - Run 2_SpatialAnalysisWells.py