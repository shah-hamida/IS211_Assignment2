import argparse
import urllib.request
import logging
import datetime
import sys


def downloadData(url):
    """Downloads the data"""
    """
       Reads data from a URL and returns the data as a string

       :param url:
       :return: the content of the URL
       """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response

def processData(csvData):
    personData = {}
    fileLines = csvData.strip().split("\n")
    for i, line in enumerate(fileLines):
        lines = line.split(",")
        try:
            person_id = int(lines[0])
            person_name = lines[1]
            person_birthday = datetime.datetime.strptime(lines[2], '%d/%m/%Y')
            personData[person_id] = (person_name, person_birthday)
        except:
            logging.error (f"Error processing line #{i} for ID #{lines[0]} because the birthday date format is wrong")
    return personData


def displayPerson(id, personData):
    if id not in personData:
        print(f"No user found with the id# {id}")
    else:
        name, birthday = personData[id]
        print(f"Person #{id} is {name} with a birthday of {birthday.strftime('%d/%m/%Y')}")


def main(url):
    print(f"Running main with URL = {url}...")
    results = downloadData(url)
    print(results)

    try:
        csvData = downloadData(args.url)
    except Exception:
        print("Error downloading data")
        sys.exit()


    personData = processData(csvData)


    while True:
        try:
            user = int(input("Enter your ID: "))

        except ValueError:
            continue
        if user <= 0:
            break
        displayPerson(user, personData)



    logger = logging.getLogger("assignment2")
    consoleHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler("errors.log")
    formatter = logging.Formatter('%(message)s')
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)



if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)




