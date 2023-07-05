# snowpack-obs-comparison-and-trends
[![DOI](https://zenodo.org/badge/627970987.svg)](https://zenodo.org/badge/latestdoi/627970987)

# Snowpack Observation Comparison and trend analysis for City of Boulder Water Resources Management Repository


### Project Rationale:

In the Western United States- where 75% of the water supply begins as snow (Nijuis, M, 2014)- snowpack data from the Natural Resource Conservation Service's Snotel Network has historically been used to predict stream flow and downstream water availability from Snow Water Equivalent (SWE). As Climate change has increased uncertainties in both the amount and timing of snowpack accumulation and snow melt, the relationship between existing Snotel site SWE data, and downstream water availability has changed. And the ability of water managers to make informed water supply decisions from Snotel data alone has become more challenging.

The City of Boulder, to better allocate, and plan for changes to its source water supply, is working to enhance the data it uses to understand seasonal snowpack, streamflow, and long-term trends through:
utilizing existing snowpack data which has been collected in, and adjacent to the North Boulder Creek Watershed as part of the Niwot Ridge Long Term Ecological Research Project (LTER), and
funding Airborne Snow Observatory flights beginning in spring of 2023 to map snow depth and model snow water equivalent (SWE) across their source water locations. 

Nijhuis, M. (2014). When the snows fail. National Geographic. Retrieved April 9, 2023, from https://www.nationalgeographic.com/west-snow-fail/ National Aeronautics and Space Administration. (n.d.). MOD10C1.006 MODIS/Terra Snow Cover Daily L3 Global 0.05Deg CMG V006. NASA Earth Observatory. Retrieved May 3, 2023, from https://earthobservatory.nasa.gov/global-maps/MOD10C1_M_SNOW

### Project Questions: 

Can existing Niwot Long Term Ecological Research (LTER) snowpack and hydrological data be used to better inform City of Boulder Water Resources Management short-term water supply decisions (source selection, leasing to agricultural partners, municipal drought declaration) or identify long-term trends in snowpack for future planning. Can this data be leveraged to increase the value of Airborne Snow Observatory flight data for water supply decision making.

### Project Outcomes:

- A python code which pulls in LTER and ASO data into an annual report or dashboard with snowpack and hydrological yearly metrics and trends relevant to City of Boulder Water Resources Management (easily readable and reproducible as new data is available each year).
- A data set of modeled historical snowpack and snowmelt timing for the upper Green Lakes Valley from existing LTER data sets (listed below).
- A data set of potential location(s) for additional ground-based to improve future ASO flight data modeling, and snowpack estimates for the upper Green Lakes Valley (and potentially for other City of Boulder source water locations).

### Instructions to set up Python Environment and Run Notebook

Detailed instructions and resources on how to set up python and create a python environment can be found here at Earth Lab's Earth Data Science online textbook and tutorials here:  https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/. Or follow the directions below.

Install the environment.yml file on your Local Computer.

To begin, install git and conda for Python 3.x.

Installing git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Installing miniconda: https://docs.conda.io/en/latest/miniconda.html

About Conda Environments: https://conda.io/docs/user-guide/tasks/manage-environments.html

Open a terminal or command line on your local computer.

Navigate to the directory where the environment.yml file lives. (This will be the directory you cloned from github for the repository).
```
$ cd snowpack-obs-comparison-and-trends
```
Create the environment using conda:
```
conda env create -f environment.yml
```
This will take a bit of time to run (sometimes up to an hour). If you want to shorten the time to solve the environment, use mamba.

First, install mamba:
```
-c conda-forge mamba
```
Then, instead of creating your environment with conda, replace conda with mamba:
```
mamba env create -f environment.yml
```
More about mamba can be found here: https://anaconda.org/conda-forge/mamba

After your environment is installed, activate the environment using:
```
conda activate snowpack-obs-python
```
The environment name is snowpack-obs-python as defined in the environment.yml file. 

(Note this is the python environment created by earthlab, where the detailed instructions are linked to, with an added package (ulmo) for downloading snotel data from CUAHSI. If you are an earth analytics certificate student, or already have the earth-anlytics-python environment installed on your local computer and want to save time, you could run the snowpack-obs notebook with this environment by just adding the ulmo package with -c conda-forge ulmo).

Once the environment has been created and activated, type
```
   jupyter notebook
```
at the command line to open the cloned repository in Jupyter with a web browser. You may now preview any of the repository files. To run the notebook, open the snow-pack-obs-comparison-and-trends.ipynb file and select 'Run All' from the Kernal drop down menu.

You may also run the notebook from the command line if you would like the outputs with out previewing the notebook with Jupyter. To do this type
```
   jupyter run snow-pack-obs-comparison-and-trends.ipynb
```
at the command line.

### Instructions to run ipython_notebook_to_html.yml Workflow

You may produce an .html version of the Ipython Notebook snowpack-obs-comparison-and-trends.ipynb file through using github actions. To run the workflow:
- From the repository main page in github, choose 'Actions' from the menu bar, then select the ipython_notebook_to_html workflow.
- Once you have selected the workflow, you can select the drop down menu 'Run Workflow' in green on the right of your screen, then from the drop down, select 'Run Workflow' again.
- An HTML file, snopack-obs-comparison-and-trends.html, will be added to the repository.
- More on github actions found here: https://github.com/features/actions

### Data Access


#### Niwot Ridge LTER Snow Observation Data Sets:
- Snow Survey Interpolated Snow Depth
- Snowpit depth, SWE, density for Niwot Ridge Saddle and Green Lakes Valley
- Snow Depth from Niwot Ridge Saddle snow grid

Data to run the analysis in the snow-pack-obs-comparison-and-trends.ipynb notebook from the Niwot Ridge Long Term Ecological Research Project (LTER) is housed on the Environmental Data Initative (EDI) Data Portal at https://portal.edirepository.org/nis/home.jsp.

To download a data package from the EDI Portal you need to define the URL with the following parameters: 

- scope
- identifier
- revision (for the most recent version of a data package 'newest' can be entered for revision)
- entityId

The download URL with then be composed of:
https://pasta.lternet.edu/package/data/eml/{scope}/{identifier}/{revision}/{entityId} 

There is a function in the repository in downloader.py for creating the URL's once the parameters are known, which are obtained from each data package in the EDI Data Repository: https://edirepository.org.

Data from the EDI Data Repository can also be downloaded directly from each data package page, which can be accessed via:

- the search page for the EDI repository: https://portal.edirepository.org/nis/advancedSearch.jsp

- the Niwot Ridge LTER data catalog search: https://nwt.lternet.edu/data-catalog

- the DataOne search engine: https://search.dataone.org/data

- the Google research dataset search engine: https://datasetsearch.research.google.com

#### Airborn Snow Observatories (ASO) Data Sets
- ASO 3m snowdepth
- ASO 50m modeled SWE

ASO data sets are available for download at: https://data.airbornesnowobservatories.com
through free sign up with ArcGIS Enterprise with ESRI, and user name and password.

#### National Resource Conservation Service Snotel Data Sets
- University Camp Snotel Site # 838 Snow Water Equivalent (SWE)
- University Camp Snotel Site # 838 Snowdepth

Snotel site descriptions and data resources can be found at: http://www.wcc.nrcs.usda.gov/snotel/
Snotel data for this notebook are accessed via theConsortium of Universities for the Advancement of Hydrologic Science, Inc Hydrologic Information Systems (CUAHSI-HIS) Water One Flow Application Programming Interface (API). More information about this service can be found here: https://his.cuahsi.org/wofws.html#wds.

There is a function in the repository downloader.py file, called in the notebook which will allow the user to download snotel data with site code and variable code inputs.
