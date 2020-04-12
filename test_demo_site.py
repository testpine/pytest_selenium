class TestDemoSite:
          
    def test_welcome(self,driver):   
        driver.get("http://demo.testpine.com")  
        welcome_text = driver.find_element_by_css_selector("h3.welcome").text
        
        assert welcome_text == 'Welcome to Testpine Demo page New'
        
    def test_login(self,driver):   
        driver.get("http://demo.testpine.com")  
        driver.find_element_by_css_selector("a[name='btnLogin']").click()
        login_form = driver.find_element_by_css_selector("h2.formLabel").text
        assert login_form == "User Login"
        
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("pwd").send_keys("password")
        driver.find_element_by_css_selector("button[type='submit']").click()
        success_txt = driver.find_element_by_css_selector("div.alert > label").text
        assert success_txt == "Success! You logged in successful."
        
        