from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep, time
# Import exceptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#keep chrome driver open we have to use chrome_options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")
    wait = WebDriverWait(driver, 2)
# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)
def Login():

    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()
    sleep(2)
    Day_name = input("Enter the day Name: ")

    Mail = wait.until(ec.visibility_of_element_located((By.ID, "email-input")))
    Mail.send_keys("osaaama@gmail.com", Keys.ENTER)


    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys("Usama1234")


    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# password=wait.until(ec.visibility_of_element_located((By.ID, "password-input")))
# password.send_keys("Usama1234")
# login = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
# login.click()
# Click Login

# Wait for schedule page to load
# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")
# Put the entire login flow into the retry-wrapper
retry(login, description="login")
# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
Days= driver.find_elements(By.TAG_NAME, "h2")

# Counters for booked classes for the booking summary
booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []
#day_group = driver.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
print(Days)
for day in Days:
    text = day.text
    print(day.text)
    param=text.split(",")
    if(param[0].strip()==Day_name ):
        print("There is tuesday")
        parentDiv = day.find_element(By.XPATH, f'./ancestor::div[contains(@id, "day-group-{Day_name.lower()}")]')
    # elif(param[0].strip()=="Thu"):
    #     parentDiv = day.find_element(By.XPATH, './ancestor::div[contains(@id, "day-group-thu")]')



Cards_data=parentDiv.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for car in Cards_data:
    time=car.find_element(By.CSS_SELECTOR, "p[id^='class-time-']")
    cut=time.text.split()
    if cut[1] == "6:00":
        class_name = car.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

        print("card information")
        book_btn=car.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
        if book_btn.text == "Booked":
          already_booked_count += 1
          print("✓ Already booked: Spin Class on Tue, Aug 12")
        elif book_btn.text=="Waitlisted":
            already_booked_count += 1
            print("✓ Already on waitlist: HIIT Class on Tue, Aug 12")
        elif book_btn.text=="book class":
            retry(lambda: book_class(button), description="Booking")

            booked_count += 1
        else:
            waitlist_count += 1
            print("✓ Joined waitlist for: Yoga Class on Tue, Aug 12")
        book_btn.click()

bookings=driver.find_element(By.ID,"my-bookings-link")
bookings.click()
print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")
print("--- DETAILED CLASS LIST ---")
# ----------------  Step 7: Verify Class Bookings on My Bookings Page ----------------

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Navigate to My Bookings page
# my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
# my_bookings_link.click()

# Wait for My Bookings page to load
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")
if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")
    # if(day.text="day-title-tue"):
    #     print("There is tuesday")
    # else:
    #     print("there is no tuesday")