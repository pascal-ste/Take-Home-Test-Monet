## The txt-file should look like this: (without the "#")
# Phrase1
# Phrase2
# ...

from selenium import webdriver

def automated_search(filename):
    search_list = []
    outcome_list = []

    f = open(filename)

    for line in f:
        search_list.append(line.strip())

    print(search_list)

    for i in search_list:
        driver = webdriver.Chrome("./chromedriver")

        driver.get("https://google.com")
        
#        I needed this part to accept google cookie settings. If this pop-up doesn't show up, this part isn't needed.
#        g_acc = driver.find_element_by_id("L2AGLb")
#        g_acc.click()

        g_search = driver.find_element_by_name("q")
        g_search.send_keys(i)

        g_search.submit()

        print("Das Suchwort ist: " + i)
        outcome_list.append("Das Suchwort ist: "+i)

        p_url = driver.find_element_by_class_name("iUh30.qLRx3b.tjvcx")
        outcome_list.append(p_url.text)
        print(p_url.text)

        p_name = driver.find_element_by_class_name("LC20lb.MBeuO.DKV0Md")
        outcome_list.append(p_name.text)
        print(p_name.text)

        driver.quit()

    return (outcome_list)

## Start this program by  inserting the path of your list-file

print(automated_search("insert_path_of_list"))
