# Drought Analysis and Creating Figures

Run these files to conduct the drought analysis and create figures from our paper where we explore groundwater and drought at different spatial scales in Arizona.

### Requirements:
Must have downloaded files and run codes described in DataPreprocessing before continuing.

### Workflow:
1. StatewideAnalysis.ipynb
    - This notebook conducts an analysis of well and GRACE data at the statewide scale
2. Regional Analysis
    - This notebook conducts a regional analysis on our filtered well database
3. Individual Wells
    - This notebook calculates the slopes and maximum drawdown of each individual well used in this analysis.  The data from this notebook was used to create statewide maps
4. Case Studies
    - This is a series of notebooks used in our case study analysis. <br>
        - a. Casestudy_analysis_AllShapes.ipynb
            - this notebook creates graphs based on a shapefile with multiple polygons.  It was created so we could have more versatility with creating graphs of our case studies.  It is basically a combination of the Regional Analysis workflow and Casestudy workflow. <br>
        - b. Casestudy_Analysis.ipynb
            - this notebook creates graphs based on a shapefile of a single polygon <br>
        - c. CasestudyAnalysis_FlagstaffSpecial.ipynb
            - this notebook was created to determine if there was skewing of the data for our flagstaff polygon.
            - there are only a few wells which match our filtering criteria so we made timeseries of those wells 
            - We then categorized them by drilling depth to create timeseries of shallow, midrange, and deep wells just for that polygon