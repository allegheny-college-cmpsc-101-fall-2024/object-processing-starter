"""Extract the data about the person from the CSV file."""

from typing import List

import csv

from objectprocessor import person

# TODO: Make sure to review the entire CSV file that is input and
# processed by this program

# TODO: note that the input people.txt file:
    # --> contains five columns
    # --> each of which contains text with a different meaning

# Sample of the data set:

# Mrs. Natalie Lee,Bolivia,036-126-0340x0094,"Engineer, building services",david82@example.org
# Michael Anderson,Honduras,(627)610-9166,Writer,ryan23@example.org
# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Andrew Johnson,Portugal,733-554-3949,"Engineer, site",michael94@example.com
# Carol Poole,Isle of Man,365.529.7270,Pensions consultant,piercebrenda@example.com


def extract_person_data(datablob: str) -> List[person.Person]:
    """Extract specific data and create persons from the provided textual contents."""
    # TODO: create an data list variable that is an empty list. N.b.
    # the empty list will be filled in the loop below.
    
    # the loop below iterates through each line of the file with the csv.reader.
    # Inside the loop, your job is to extract or parse all relevant details from
    # each line.
    for line in csv.reader(
        datablob.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # TODO: extract each of the attributes about a person from the line variable
        # TODO: construct a new instance of the Person class that contains all
        # of the attributes that were extracted from the CSV file
        # TODO: append the current instance of the person class to the data_list variable
    # TODO: return the data list


def write_person_data(file_name: str, person_data: List[person.Person]) -> None:
    """Write the person data stored in a list to the specified output file."""
    # TODO: create an empty storage list that will store the person data as a list of strings
    # TODO: iterate through every person inside of the person_data list
        # TODO: create a list out of this person where each of the person's
        # attributes are stored inside of an index in the list
        # TODO: append this converted person list to the storage list
    # TODO: use the csv.writer approach and the writerows function to write out
    # the list of lists of strings that contain all of the person data
    # https://docs.python.org/3/library/csv.html


def find_matching_people(
    attribute: str, match: str, person_data: List[person.Person]
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""
    # TODO: create an empty matching list to which Persons who have an
    # attribute matching the search term in match will be added
    # TODO: iterate through all of the people in the person_data list.
    # inside this loop, you should use the function below!
        # TODO: if the current person has an attribute that contains the search term in match
            # TODO: then add the current person to the matching list list
    # TODO: return the list that contains the Persons with matches


def is_matching_person(
    attribute: str, match: str, search_person: person.Person
) -> bool:
    """Determine if the person's specified attribute contains the search term in match."""
    # TODO: the attribute for matching is name
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is country
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is phone number
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is job
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # TODO: the attribute for matching is email
      # TODO: return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # return False if none of the conditions are matching
