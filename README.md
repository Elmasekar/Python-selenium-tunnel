# How to start tunnel for automation test in Python-selenium on [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=Python-selenium-tunnel)

If you want to run your an automation test in Python-selenium on LambdaTest using the tunnel and want to start the tunnel automatically in the script, you can use the follwing steps. You can refer to sample test repo [here](https://github.com/LambdaTest/python-selenium-sample).

## Steps

### Step 1: Download the LT tunnel binary from LT Dashboard

Go to your LambdaTest dashboard and click the configure tunnel button on the top right corner and use the download link to download the binary file. 

### Step 2: Code to run LT tunnel before test

The tunnel should be started before test case execution and end after completion. To achieve this, tunnel can be started in the main function like so: 


```python
import subprocess

if __name__ == "__main__":

    #start tunnel process
    tunnel_process = subprocess.Popen(["./LT","--user",username,"--key",access_key],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    
    #run testcases
    unittest.main()

    #end tunnel
    tunnel_process.terminate()
```
### Step 3: Set tunnel capability to True

Add the `"tunnel": True`  capability in your test file:

```python
desired_caps = {
            'LT:Options': {
                "build": "Python Demo",  # Change your build name here
                "name": "Python Demo Test",  # Change your test name here
                "platformName": "Windows 11",
                "selenium_version": "4.0.0",
                "tunnel": True
            },
            "browserName": "Chrome",
            "browserVersion": "98.0",
        }

```

### Step 4: Run your test

```bash
python lambdatest.py
```


# Links:

[LambdaTest Community](http://community.lambdatest.com/)

