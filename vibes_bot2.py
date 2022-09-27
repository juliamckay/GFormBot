from utils import *

if __name__ == "__main__":
    driver = setup_method()
    count = 0

    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSe5TQPM2JxMi3jfEwMB9z1EkFCy997v06rvaSaj0vj5jjD7Hw/viewform")
    driver.set_window_size(1898, 1018)
    time.sleep(2)

    while True:
        vote_bees(driver)