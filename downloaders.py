# Import libraries for download functions
import os
import pathlib

import earthpy as et
import numpy as np
import pandas as pd
import ulmo


def edi_dataset_url(scope, identifier, revision, entityid):
    """
    Create download URL for EDI data sets.

    Data sets for EDI repository are found at
    https://edirepository.org
    and require unique parameters for each
    data set which can be loaded into the
    parameters for this function.

    Parameters:
    ----------
    scope : str
        Unique scope found on EDI portal for each data package.

    identifier : str
        Data set package number.

    revision : str
        Version number of data set.

    entityid : str
        Unique id for each data set of a data package.

    Returns
    -------
    edi_url : EDI data set url for downloading.
    """
    # Define package url
    edi_url = (
        "https://pasta.lternet.edu/package/data/eml/"
        "{scope}/{identifier}/{revision}/{entityid}"
    .format(scope=scope, identifier=identifier,
            revision=revision, entityid=entityid))
    return edi_url

def edi_dataset_download(
        dataset_name, scope, identifier, revision, entityid):
    """
    Download Niwot Ridge LTER streamflow data set from EDI portal.

    Data sets for EDI repository are found at
    https://edirepository.org.

    Parameters:
    ----------
    dataset_name : str
        Name of data set.

    scope : str
        Unique scope found on EDI portal for each data package.


    identifier : str
        Data set package number.

    revision : str
        Version number of data set. Set to 'new'
        for most recent version.

    entityid : str
        Unique id for each data set of a data package.

    Returns
    -------
    edi_url : EDI data set url for downloading.
    """
    
    # Define package url
    edi_url = (
        "https://pasta.lternet.edu/package/data/eml/"
        "{scope}/{identifier}/{revision}/{entityid}"
        .format(scope=scope, identifier=identifier,
                revision=revision, entityid=entityid))

    # Create directory for data set
    dataset_dir = '{dataset_name}'.format(dataset_name=dataset_name)

    # Make data set directory if doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    # Define path for data set
    path = os.path.join(dataset_dir, '{dataset_name}'
                        .format(dataset_name=dataset_name))

    # Download data frame if not cached and set date to index
    if not os.path.exists(path):
        dataset_df = pd.read_csv(edi_url)
        dataset_df.to_csv(path)
    dataset_df = pd.read_csv(path)
    dataset_df['date'] = pd.to_datetime(dataset_df['date'])
    dataset_df = dataset_df.set_index('date')

    # Return data frame
    return dataset_df

def snotel_dataset_download(
    site_code, value_code, start_date, end_date, 
    value_name, dataset_name, file_name):
    """
    Download snotel data and convert values to Pandas Data Frame,
    cache data frame as .csv file.
    
    Parameters:
    ----------
    site_code : str
        Snotel site code.
        
    variable_code : str
        Variable code.
        
    start_date : str
        Start date to download data from.
        
    end_date : str
        End date to download data from.
    
    value_name : str
        Name of value column.
    
    data_set_name : str
        Name of directory for data set.
    
    file_name : str
        Name of file for data.
    
    Returns:
    --------
        Pandas data frame of desired snotel site values.
"""
    # Get dictionary of snow depth values for site of interest using ulmo
    snotel_value_dict = ulmo.cuahsi.wof.get_values(
    'https://hydroportal.cuahsi.org/Snotel/cuahsi_1_1.asmx?WSDL',
    site_code, value_code, start_date, end_date)

    # Convert dictionary to pandas data frame
    snotel_value_df = pd.DataFrame.from_dict(snotel_value_dict['values'])
      
    # Change datetime to pandas object and set to index
    snotel_value_df['datetime'] = pd.to_datetime(snotel_value_df['datetime'])
    snotel_value_df = snotel_value_df.set_index('datetime')
    
    # Convert values to float, replace nodata values with NaN
    snotel_value_df['value'] = pd.to_numeric(
        snotel_value_df['value']).replace(-9999, np.nan)
    
    # Drop values w/ low quality flag
    snotel_value_df = snotel_value_df[
        snotel_value_df['quality_control_level_code'] == '1']
    
    # Rename value column to expressive variable name
    snotel_value_df = snotel_value_df.rename(
        columns = {'value':'{value_name}'.format(value_name=value_name),
                  'datetime':'date'})
    
    # Create directory for data set
    dataset_dir = '{dataset_name}'.format(dataset_name=dataset_name)

    # Make data set directory if doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    # Define path for data set
    path = os.path.join(dataset_dir, '{file_name}'
                        .format(file_name=file_name))

    # Download data frame if not cached
    if not os.path.exists(path):
        snotel_value_df.to_csv(path)

    return snotel_value_df