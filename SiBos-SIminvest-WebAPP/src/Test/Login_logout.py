

from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
        page = browser.new_page()
        page.goto("https://stg-sibos.siminvest.co.id")

        # Locate the username and password fields by their 'id' or 'name' attributes and fill them
        page.fill("#username", "admin@example.com")  # Fills in the username field using its id
        page.fill("#password", "admin123")  # Fills in the password field using its id
        page.click("button:has-text('Sign In')")
        page.click("p:has-text('Referral Reward')")
        page.click("span:has-text('Sign Out')")
        page.wait_for_timeout(5000)  # Wait for 5 seconds to observe the page
        input("Press Enter to close the browser...")

        browser.close()
if __name__ == "__main__":
    test_login()


