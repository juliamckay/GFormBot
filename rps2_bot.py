from rps2_utils import *

if __name__ == "__main__":
    count = 0
    driver = setup_method()

    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSfADYdCgdF4VvT95Myt_cbp7FO_9A0v-Z-fdYmcyfoagV4_DA/viewform")
    driver.set_window_size(1898, 1018)
    time.sleep(2)

    #selection menu
    print("1 - vote all"
          "2 - vote jules' favs"
          "3 - vote top 2"
          "4 - vote top 1"
          "")
    selection = input("Please select an option: ")

    while True:
        count += 1
        try:
            if selection == "1":
                vote_all(driver)
            elif selection == "2":
                vote_jules_favs(driver)
            elif selection == "3":
                vote_top_two(driver)
            elif selection == "4":
                vote_top_1(driver)
        except:
            print("ran " + count + " times.")