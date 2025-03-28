from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Music:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'))

    def play(self, query):
        self.query = query
        # Open YouTube search results for the given query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        try:
            # Wait for the video results to load and locate the first video title
            video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]'))
            )
            print("Video found, clicking on it...")
            video.click()  # Click on the first video
            
            # Optional: wait to let the video play
            WebDriverWait(self.driver, 600).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="html5-main-video"]'))
            )  # Wait for the video to load
            print("Video is now playing.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Clean up: quit the driver after a delay or when you're done
            # You may choose to keep the driver open for a longer period if needed
            self.driver.quit()

# assist = Music()
# assist.play("believer song")  # Replace with your desired song title
