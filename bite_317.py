from datetime import date
import os
from pathlib import Path
import pickle
from typing import Sequence, NamedTuple
from urllib.request import urlretrieve

url = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = "https://bites-data.s3.us-east-2.amazonaws.com/input.pkl"
PICKLE_OUTFILE = "https://bites-data.s3.us-east-2.amazonaws.com/output.pkl"


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


def download_pickle_file():
    """download a pickle file we created with a
       list of namedtuples
    """
    download = urlretrieve(url)
    return download

def deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    f = urlretrieve(PICKLE_INFILE)
    with pkl_file.open('rb') as f:
        return pickle.load(f)

def serialize(pkl_file: Path = PICKLE_OUTFILE,
              data: Sequence[NamedTuple] = None) -> None:
    """Save the data passed in to the pickle file passed in"""
    f = urlretrieve(PICKLE_OUTFILE)
    if data is None:
        data = deserialize()

    with pkl_file.open('wb') as f:
        pickle.dump(data, f)
