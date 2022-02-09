# importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# the webpage link
youtube_trending_url_link = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

# function to put driver options
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('D:/Software/Professional Software/Chrome-Driver/chromedriver_win32/chromedriver', 
                              options=chrome_options)
    return driver

# function to get videos
def get_videos(driver):
    driver.get(youtube_trending_url_link)
    video_tag_divs = 'ytd-video-renderer'
    video_divs = driver.find_elements(By.TAG_NAME, video_tag_divs)
    return video_divs
    
if __name__ == "__main__":
    print("Creating driver")
    driver = get_driver()
    
    print("Fetching the page")
    videos = get_videos(driver)
    
    print(f'Found {len(videos)} videos')
    































