from utils import *

if __name__ == "__main__":
    driver = setup_method()

    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSfnhCteXlhnKrR4jQSl1dh_Gl8i4p9DRhLf5juFXbe_u2tcaA/viewform")
    driver.set_window_size(1898, 1018)
    time.sleep(2)

    while True:
        vote_multi(driver)