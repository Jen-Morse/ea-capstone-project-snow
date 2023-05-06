# Import libraries for download functions
import os
import pathlib

import earthpy as et
import pandas as pd


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