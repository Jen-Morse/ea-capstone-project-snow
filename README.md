# ea-capstone-project-snow

# Earth Analytics Capstone Project:
# Snow Observations Comparison for City of Boulder Water Resources Management 

### Project Questions: 

Can existing Niwot Long Term Ecological Research (LTER) snowpack and hydrological data be used to better inform City of Boulder Water Resources Management short-term water supply decisions (source selection, leasing to agricultural partners, municipal drought declaration) or identify long-term trends in snowpack for future planning. Can this data be leveraged to increase the value of Airborne Snow Observatory flight data for water supply decision making.

### Project Outcomes:

- A python code which pulls in LTER and ASO data into an annual report or dashboard with snowpack and hydrological yearly metrics and trends relevant to City of Boulder Water Resources Management (easily readable and reproducible as new data is available each year).
- A data set of modeled historical snowpack and snowmelt for the upper Green Lakes Valley from existing LTER data sets (listed below).
- A data set of potential location(s) for additional ground-based to improve future ASO flight data modeling, and snowpack estimates for the upper Green Lakes Valley (and potentially for other City of Boulder source water locations).

### Environment Requirements

To  set up the environment.yml python environment needed to run this notebook, follow the instructions at:  https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/

### Data Access

#### Niwot Ridge LTER Snow Observation Data Sets:
- Snow Survey Interpolated Snow Depth
- Snowpit depth, SWE, density for Niwot Ridge Saddle and Green Lakes Valley
- Snow Depth from Niwot Ridge Saddle snow grid

Data to run the analysis in the Snow Observations Comparison Notebook from the Niwot Ridge Long Term Ecological Research Project (LTER) is housed on the Environmental Data Initative (EDI) Data Portal at https://portal.edirepository.org/nis/home.jsp.

To download a data package from the EDI Portal you need to define the URL with the following parameters: 

- scope
- identifier
- revision (for the most recent version of a data package 'newest' can be entered for revision)
- entityId

The download URL with then be composed of:
https://pasta.lternet.edu/package/data/eml/{scope}/{identifier}/{revision}/{entityId} 

There is a function in the notebook for creating the URL's once the parameters are known, which are obtained from each data package in the EDI Data Repository: https://edirepository.org.

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

*Note that because Boulder Creek Watershed ASO flights for spring of 2023 have not yet occurred, this data is not currently available and not included in the current notebook.


