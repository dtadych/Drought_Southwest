# Data Preprocessing

Run items in this folder to move on to drought analysis.

### Requirements:
 - Download ADWR's groundwater databases.
   - <a href = ''>Well Registry </a>: catalog of all well permits in Arizona
   - <a href= 'https://www.azwater.gov/sites/default/files/zip/GWSI_ZIP_20240401.zip'>Groundwater Site Inventory (GWSI)</a>: long-term water level measurements
      <br> - *Note* - This code uses the excel form of this database found on a different webpage than Well Registry. 
   - Make sure to unzip all files, then move to Data/Input/Shapefiles folder
 - Download the latest <a href=' https://www2.csr.utexas.edu/grace/RL0602_mascons.html'>GRACE data</a>.
 - Move these files into the Data/Input/Shapefiles folder.
 - Download "georeg_reproject_fixed" files from our <a href=' https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/Tadych_AzGroundwaterSpatialAnalysis_Aug2023/Data/Shapefiles'>Cyverse database </a>

 - Place in Data/Input/Shapefiles folder.
 
 - Download Drought indices
   - The dataset needed is from NOA National Centers for Environmental Information averaged for the state of Arizona.
   - <a href='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/2/pdsi/1/0/1895-2024'> Link to download PDSI</a>, save it as "NOAA_PDSI_Timesseries.csv" in Data/Input folder
   - <a href='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/2/phdi/1/0/1895-2024'>Link to download PHDI </a>, save it as "NOAA_PHD_Timesseries.csv" in Data/Input

 ### Run Codes
 1. First, need to merge the well databases.  Make sure all filepaths match where the new data has landed.
    - Run 1_WellStaticMerge.py
      - This database contains all static information about the wells from both databases
    - Run 1_WellTSMerge.py
      - This database pulls water level data from both databases to create timeseries of all wells (even if some wells just have one reading)
 2. Second, run spatial analysis scripts
    - Run 2_SpatialAnalysisGrace.py
      - This script creates a state average of total water storage
    - Run 2_SpatialAnalysisWells.py
      - This script filters our well database to export wells with at least 15 years of data or more (used for graphing later)
      - Creates water level values by groundwater regulation and by access to surface water
 3. Third, run DroughtIndices.py
    - This script will create yearly averages of pdsi and phdi into a nice and cozy dataset