"""Input and process objects about people."""

from pathlib import Path

from typing import List

import typer

from rich.console import Console

from objectprocessor import process
from objectprocessor import person

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


def stringify_list_for_display(person_list: List[person.Person]) -> str:
    """Process the list of people for display in the console."""
    # TODO: Notice the input type annotation for person_list. The
    # job of this function is to take that list and turn it into
    # a well-formatted string. A different part of the code will
    # then print the string to the console. Here is the pseudo code:
    #
    # Create an empty string that will eventually contain all of the
    # text. Iterate through each of the people in the person_list and
    # add all of their textual details to the string; make sure to
    # preface each entry with a "-" and add a newline character at
    # the end. Finally, return the full string.


@cli.command()
def main(
    search_term: str = typer.Option(...),
    attribute: str = typer.Option(...),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""
    # TODO: refer to the expected output portion of the readme to
    # see what this function should display. Add a line of code
    # below each of the following pseudo-code comments.
    # TODO: display details about the input file provided on the command line
    # TODO: if input file was not found, we cannot continue using program
    # --> TODO: display diagnostic messages about the incorrect file
    # TODO: if the file was specified and it is valid, we should read and check it
    # --> TODO: read in the data from the specified file containing information about people
    # --> TODO: transform the data in the CSV file (now in a string) into a list of instances of the Person class
    # --> TODO: search for the people with an attribute that matches the search term
    # --> TODO: display the details about the matching people to the console
    # --> TODO: make sure to use the stringify_list_for_display function for creating a suitable display
    # --> TODO: save the details about the matching people to the file system in the specified output directory
