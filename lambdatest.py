import os
import unittest
import sys
from selenium import webdriver

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

	# setUp runs before each test case
	def setUp(self):
		desired_caps = {
			'LT:Options': {
				"user": username,
				"accessKey": access_key,
				"build": "UnitTest-Selenium-Sample",
				"name": "UnitTest-Selenium-Test",
				"platformName": "Windows 11",
				"selenium_version": "4.0.0",
				"tunnel": True,
			},
			"browserName": "Chrome",
			"browserVersion": "latest",
		}

		self.driver = webdriver.Remote(
			command_executor="http://hub.lambdatest.com:80/wd/hub",
			desired_capabilities=desired_caps)


# tearDown runs after each test case

	def tearDown(self):
		self.driver.quit()

	def scroll_bottom():
		"""
		Verify scrolling to bottom
		:return: None
		"""
		driver.get('https://www.lambdatest.com/')
		driver.maximize_window()
		sleep(2)
		success = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(5)


if __name__ == "__main__":

	#start tunnel process
	tunnel_process = subprocess.Popen(["./LT","--user",username,"--key",access_key],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
	
	#run testcases
	unittest.main()

	#end tunnel
	tunnel_process.terminate()
