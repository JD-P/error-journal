import argparse
import time
from bs4 import BeautifulSoup


def error_form(journalpath):
    """The form a user fills out when they choose the error entry type."""
    entry_time = gen_iso_8601()
    program = input("What program did the error occur in?")
    description = field_multiline("Describe the nature of the error.")
    hypothesis = field_multiline("What do you think is causing the error?")
    etc = field_etc("How long do you expect it to take to fix this error?")

def update_form(journalpath):
    pass

def resolution_form(journalpath):
    pass

def field_multiline(display_text):
    """Print the display text and get multiple lines of input from the user.
    Returning a list of lines after '^^' is sent by itself as a single line to 
    the interface."""
    last_line = ""
    lines = []
    print(display_text)
    while last_line != "^^":
        lines.append(input(">"))
    return lines

def field_etc(display_text):
    """Print the display text and get a single line of text from the user which
    conforms to the day minute second time format."""
    correct = False
    while correct is False:
        etc = input(display_text)
        correct = True # Default is that etc is correct until a check makes it incorrect
        for character in etc:
            if character not in "0123456789dms":
                print("ETC was not given in day minute second format. Example:",
                      " 1d1m1s.")
                correct = False
        if etc.count("d") > 1 or etc.count("m") > 1 or etc.count("s") > 1:
            correct = False
    return etc
            

def gen_iso_8601():
    """Generate an ISO 8601 date+time stamp for the current time in UTC."""
    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

parser = argparse.ArgumentParser()
parser.add_argument("entry_type", 
                    help=("The type of entry you are making. Options are error," +
                          " update and resolution."))
parser.add_argument("journalpath", help="The filepath to the journal you're modifying.")
arguments = parser.parse_args()

if arguments.entry_type == "error":
    error_form(arguments.journalpath)
elif arguments.entry_type == "update":
    update_form(arguments.journalpath)
elif arguments.entry_type == "resolution":
    resolution_form(arguments.journalpath)
else:
    print("'" + arguments.entry_type + "' is not a valid entry type. Use error, ",
          "update or resolution instead.")

