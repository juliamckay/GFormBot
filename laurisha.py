from utils import *

if __name__ == "__main__":
    driver = setup_method()

    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSfpND3k51SNWqfMDPSUvYP69GNCwnz8RAW4y1J3jjldfJccNw/viewform")
    driver.set_window_size(1898, 1018)
    time.sleep(2)

    while True:
        vote_laurisha(driver)