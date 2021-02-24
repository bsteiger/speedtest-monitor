import json
import logging
from os import path, mkdir, getenv
from time import sleep
from speedtest import Speedtest, SpeedtestResults
from dotenv import load_dotenv

FILE = None

# Load ENV globals
load_dotenv()
RESULTS_PATH = path.normpath(getenv("RESULTS_PATH", "./results"))
TEST_INTERVAL_SECS = getenv("TEST_INTERVAL_SECS", 900)


def log_results(results: SpeedtestResults):
    print(
        f"[{results.timestamp}]\tDown:\t{results.download/10**6:.2f}Mbps\n\t\t\t\tUp:\t{results.upload/10**6:.2f}Mbps"
    )
    # global FILE
    # if FILE is None:
    FILE = path.join(RESULTS_PATH, f"{results.timestamp}.json")
    with open(FILE, 'w+') as f:
        f.write(results.json(pretty=True))


while True:
    # Initialize a new speedtest and run it
    speedtest = Speedtest()
    print("Running download test...")
    speedtest.download()
    print("Running upload test...")
    speedtest.upload()

    # Do something with the results
    log_results(speedtest.results)
    sleep(TEST_INTERVAL_SECS)
