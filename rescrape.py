import pandas as pd
import numpy as np
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

df = pd.read_csv("final_data.csv", sep="~")
df = df.replace('Nan', np.nan)
new_df = df.dropna(axis=0, how='any', inplace=False)

new_df.to_csv("final_data_no_na.csv", sep="~")
new_df["description"] = np.nan
print(new_df)

#SCRAPER PART BELOW IGNORE ABOVE
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = uc.Chrome(options=options)
all_strings = []

for i in range(len()):
    link = new_df.iloc[i, 13]    
    # Navigate to Zillow
    driver.get(link)

    content = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-testid='description'] | //*[@data-testid='property-description']")))
    button = content[0].find_element(By.TAG_NAME, "button")
    button.click()

    all_strings.append(content[0].text)
    time.sleep(1)
    new_df.iloc[i, 15] = content[0].text
    print(link)
    new_df.to_csv("data_with_description.csv", sep="~")

new_df["description"] = all_strings
# df = df[df['water'] == np.nan]

