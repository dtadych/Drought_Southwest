# Impact of Groundwater Management on Drought Responses in the Southwest
*Danielle E. Tadych, Bonnie G. Colby, Laura E. Condon*

This repository is for our paper "Impact of Groundwater Management on Drought Responses in the Southwest."  To use this repository, please cite 
> Tadych, D.E., Colby, B.G., Condon, L.E. (2024). *Impact of Groundwater Management on Drought Responses in the Southwest* [Unpublished manuscript]. Department of Hydrology and Atmospheric Sciences, University of Arizona.

To get started, set up your environment using the environment.yml.  

Then, move on to Code/DataPreprocessing to begin the analysis.  Follow all instructions in the readme (repeated below).

## Data Preprocessing

Run items in this folder to move on to the drought analysis (FigureCreation).

### Requirements:
 1. Download ADWR's groundwater databases.
     - <a href = 'https://gisdata2016-11-18t150447874z-azwater.opendata.arcgis.com/datasets/34c92af536ec4047aeaf9d93053dc317_0/explore?location=0.015556%2C-111.970052%2C0.00' target='_blank'>Well Registry </a>: catalog of all well permits in Arizona
       - First, save it as csv in Data/Input as "Well_Registry_[mmddyyyy].csv
       - Next, save it as a shapefile in Data/Input/Shapefiles folder
       - Make sure to unzip all files
     - Groundwater Site Inventory (GWSI)</a>: long-term water level measurements
       - First, save the <a href= 'https://www.azwater.gov/sites/default/files/zip/GWSI_ZIP_20240401.zip' target='_blank'>excel form of the database here</a> from the main website into Data/Input
        <br>  - *Note* - This code uses the excel form of this database found on a different webpage than the gis files.
       - Next, save it as a shapefile from the <a href='https://gisdata2016-11-18t150447874z-azwater.opendata.arcgis.com/datasets/azwater::gwsi-app/explore?layer=3&location=34.064362%2C-111.834805%2C6.67' target='_blank'>ADWR GIS Data repository here</a> into Data/Input/Shapefiles folder
       - Make sure to unzip all files
2. Download the latest <a href='https://www2.csr.utexas.edu/grace/RL0602_mascons.html' target='_blank'>GRACE data</a>.
   - Move these files into the Data/Input/Shapefiles folder.
3. Download "georeg_reproject_fixed" files from our <a href='https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/Tadych_AzGroundwaterSpatialAnalysis_Aug2023/Data/Shapefiles' target='_blank'>Cyverse database </a>
   - Place in Data/Input/Shapefiles folder.
 
 4. Download Drought indices
     - The dataset needed is from NOAA National Centers for Environmental Information averaged for the state of Arizona.
     - <a href='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/2/pdsi/1/0/1895-2024' target='_blank'> Link to download PDSI</a>, save it as "NOAA_PDSI_Timeseries.csv" in Data/Input folder
     - <a href='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/2/phdi/1/0/1895-2024' target='_blank'>Link to download PHDI </a>, save it as "NOAA_PHDI_Timeseries.csv" in Data/Input folder

 ### Run Codes
 1. First, need to merge the well databases.  Make sure all filepaths match where the new data has landed.
    - Run 1a_WellStaticMerge.py
      - This code creates databases that contain all static information about the wells from ADWR
    - Run 1b_WellTSMerge.py
      - This code pulls water level data from both databases to create timeseries of all wells (even if some wells just have one reading)
 2. Second, run spatial analysis scripts
    - Run 2a_SpatialAnalysisGrace.py
      - This script creates a state average of total water storage
    - Run 2b_SpatialAnalysisWells.py
      - This script filters our well database to export wells with at least 15 years of data or more (used for graphing later)
      - Creates water level values by groundwater regulation and by access to surface water
 3. Third, run 3_DroughtIndices.py
    - This script will create yearly averages of pdsi and phdi into a nice and cozy dataset

## Drought Analysis and Creating Figures

Run these files to conduct the drought analysis and create figures from our paper where we explore groundwater and drought at different spatial scales in Arizona.

The concept of our workflow is illustrated in the picture shown below.
![Flowchart showing how Depth to Water readings (DTW) are plotted against time to create a trendline (least squares regression).  The DTW values are then subtracted by the trendline to calculate anomalies.  Anomalies are plotted against time.  Maximum drawdown is the maximum anomaly within a severe drought period.](Figures/Figure1.png)

### Requirements:
Must have downloaded files and run codes described in DataPreprocessing before continuing.

### Workflow:
1. StatewideAnalysis.ipynb
    - This notebook conducts an analysis of well and GRACE data at the statewide scale.
    - Creates Figures 3-4.
2. RegionalAnalysis.ipynb
    - This notebook conducts a regional analysis on our filtered well database.
    - Creates Figures 5-6
3. IndividualWells.ipynb
    - This notebook calculates the slopes and maximum drawdown of each individual well used in this analysis.  The data from this notebook was used to create statewide maps.
    - outputs data used for Figure 7, although Figure 7 was created in QGIS.
4. Case Studies
    - This is a series of notebooks used in our case study analysis. <br>
        - a. Casestudy_analysis_AllShapes.ipynb
            - this notebook creates graphs based on a shapefile with multiple polygons.  It was created so we could have more versatility with creating graphs of our case studies.  It is basically a combination of the Regional Analysis workflow and Casestudy workflow (see b). <br>
            - Creates Figures 8-10 except for maps which were created in QGIS
        - b. Casestudy_Analysis.ipynb (optional)
            - this notebook creates graphs based on a shapefile of a single polygon <br>
            - It can be used for preliminary analysis.
        - c. CasestudyAnalysis_FlagstaffSpecial.ipynb (optional)
            - this notebook was created to determine if there was skewing of the data for our Flagstaff polygon.
            - there are only a few wells which match our filtering criteria so we made timeseries of those wells.
            - We then categorized them by drilling depth to create timeseries of shallow, midrange, and deep wells just for that polygon.

You're done!  Go check out your new figures created in the Figures folder.  Compare it to items in "Correct" to see if you got the same output!