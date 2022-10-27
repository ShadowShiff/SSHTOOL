import os


print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")
    os.system("pip install colorama")
    os.system("pip install time")
    os.system("pip install os")
    os.system("pip install random")
    os.system("pip install queue")
    os.system("pip install optparse")
    os.system("pip install sys")
    os.system("pip install socket")
    os.system("pip install treading")
    os.system("pip install logging")
    os.system("pip install request")
    os.system("pip install random")


elif c == "1":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
    os.system("pip3 install colorama")
    os.system("pip3 install time")
    os.system("pip3 install os")
    os.system("pip3 install random")
    os.system("pip3 install queue")
    os.system("pip3 install optparse")
    os.system("pip3 install sys")
    os.system("pip3 install socket")
    os.system("pip3 install treading")
    os.system("pip3 install logging")
    os.system("pip3 install request")
    os.system("pip3 install random")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")