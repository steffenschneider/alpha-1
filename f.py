# coding=utf-8

import datetime
import os
import sys
import urllib
from time import gmtime, strftime, localtime

from selenium import webdriver


# os-functions ############################################################


def get_os_name() -> str:
    """ e.g. posix, nt """
    result = os.name
    if result == 'posix':
        print("Linux System")
    if result == 'nt':
        print("Windows System")
    else:
        print("Unknown System")
    return result


def change_dir(path):
    os.chdir(path)


def get_current_path() -> str:
    result = os.getcwd()
    return result


def get_script_path():
    result = os.path.dirname(os.path.abspath(__file__))
    return result


def is_dir_available(path) -> bool:
    import os
    result = os.path.isdir(path)
    return result


def is_file_available(path) -> bool:
    import os
    result = os.path.exists(path)
    return result


# time-functions ########################################


def get_mod() -> str:
    get_minute_of_the_day()


def get_minute_of_the_day() -> str:
    hour = strftime("%H", localtime())
    minute = strftime("%M", localtime())
    minute_of_the_day = int(hour) * 60 + int(minute)
    print(str(minute_of_the_day))
    return str(minute_of_the_day)


def get_seconds_since_1970_with_microseconds():
    import time
    ts = time.time()
    return ts


def get_seconds_since_1970_without_microseconds():
    import time
    import math
    ts = time.time()
    ts = math.floor(ts)
    return ts


def get_local_time():
    time_now = strftime("%H:%M:%S", localtime())  # local time
    return time_now


def get_time():
    time_ = get_local_time()
    print(time_)
    return time_


def get_utc_time():
    time_now = strftime("%H:%M:%S", gmtime())  # utc
    print(time_now)
    return time_now


def get_second():
    time_now = strftime("%S", localtime())
    return time_now


def get_date():
    date = strftime("%d.%m.%Y", localtime())  # local time
    return date


def get_datetime():
    datetime_ = strftime("%d.%m.%Y %H:%M:%S", localtime())  # local time
    return datetime_


def get_weekday():
    """
    0 --> Monday
    6 --> Sunday
    I will add 1
    1 --> Monday
    7 --> Sunday
    """
    result = datetime.datetime.today().weekday() + 1
    print(result)
    return result


# open links #########################################################


def open_dlf():
    import webbrowser
    url = "http://srv.deutschlandradio.de/themes/dradio/script/aod/index.html?audioMode=2&audioID=4&state="
    new = 2  # open in a new tab, if possible
    webbrowser.open(url, new=new)


def open_hintergrund():
    import webbrowser
    url = "http://www.deutschlandfunk.de/podcast-hintergrund.725.de.podcast.xml"
    new = 2  # open in a new tab, if possible
    webbrowser.open(url, new=new)


def open_cuk():
    open_computer_und_kommunikation()


def open_computer():
    open_computer_und_kommunikation()


def open_computer_und_kommunikation():
    import webbrowser
    url = "http://www.deutschlandfunk.de/podcast-computer-und-kommunikation-komplette-sendung.416.de.podcast.xml"
    new = 2  # open in a new tab, if possible
    webbrowser.open(url, new=new)


##################################################


def get_ip() -> str:
    get_my_ip()


def get_my_ip() -> str:
    # myip = socket.gethostbyname(socket.gethostname())
    myip = os.system("ifconfig | awk '/inet addr/{print substr($2,6)}'")
    print(myip)
    return myip


def upgrade_linux():
    sudo_password = input("sudo password: ")
    command = 'apt-get update'
    os.system('echo %s|sudo -S %s' % (sudo_password, command))
    command = 'apt-get upgrade -y'  # -y for typing yes
    os.system('echo %s|sudo -S %s' % (sudo_password, command))


def check_if_root() -> bool:
    if os.geteuid() == 0:
        return True
    else:
        return False


def check_wlan() -> bool:
    url = "http://www.google.de"
    try:
        if urllib.request.urlretrieve(url, "/home/kame/test.txt"):
            print("Connected to the internet")
            return True
    except ConnectionError:
        print("Not connected to the internet!!!")
        return False


def get_temperature() -> str:
    from pyvirtualdisplay import Display

    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Firefox()
    url = "http://www.yr.no/sted/Tyskland/Baden-W%C3%BCrttemberg/Bad_S%C3%" \
          "A4ckingen/time_for_time.html"
    driver.get(url)
    result = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[3]/table[1]/tbody/tr[1]/td['
                                          '3]').get_attribute('innerHTML')
    result = result[:-1]  # don't show degree sign
    driver.close()

    display.stop()
    print("It is " + result + " degrees.")
    return result


def get_news():
    if check_wlan():
        from pyvirtualdisplay import Display
        import re

        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = webdriver.Firefox()
        url = "http://www.deutschlandfunk.de/"
        driver.get(url)
        source = driver.find_element_by_xpath('//*[@id="wrapper"]/div/section[2]/div[1]').get_attribute('innerHTML')

        n_articles = source.count('<article')
        print(str(n_articles) + " articles found.")

        lst = re.findall('<h3>(.+)</h3>', source)
        result = lst

        driver.close()

        display.stop()
        return result
    else:
        print("Error: Not connected to the internet")


def get_filenames_from_dir(path):
    import glob
    path += "*.mp3"
    return glob.glob(path)


def get_installed_modules() -> list:
    import pip
    installed_packages = pip.get_installed_distributions()
    # installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    #     for i in installed_packages])
    installed_packages_list = sorted(["%s" % i.key for i in installed_packages])
    return installed_packages_list


def battery() -> str:
    get_battery_status_in_percent()


def get_battery_status_in_percent() -> str:
    #
    path = "/sys/class/power_supply/BAT0/energy_now"
    if is_dir_available(path):
        pass
    else:
        path = "/sys/class/power_supply/BAT0/charge_now"
    now_ = open(path).read()
    # print("now: " + str(now_))

    path = "/sys/class/power_supply/BAT0/energy_full"
    if is_dir_available(path):
        pass
    else:
        path = "/sys/class/power_supply/BAT0/charge_full"
    full_ = open(path).read()
    # print("full: " + str(full_))

    result = 100.0 * int(now_) / int(full_)
    result = str("{0:.1f}".format(result))
    print("battery: " + result + " %")
    if float(result) < 20.0:
        print("###########################################")
        print("###########################################")
        print("#########      low - battery      #########")
        print("###########################################")
        print("###########################################")
    return result


def count_functions() -> str:
    count_my_functions()


def count_my_functions() -> str:
    import re
    path = "/home/kame/Dropbox/code/python/scripts/f.py"
    lst = []
    for line in open(path):
        # count the word def in this file
        # don't count the word def in this function more than once
        lst += re.findall(r'def ([a-z]){3,}', line)
    print(str(len(lst)) + " functions available in f.py")


def run_bot():
    from pyvirtualdisplay import Display
    import re

    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Firefox()
    url = "http://www.heise.de"
    print("I will visit " + url + " now")
    driver.get(url)

    # retrieve title of each article
    # xpath = './/*[@id="zeile_e"]/div[1]/a/h2'
    # xpath2 = './/*[@id="zeile_e"]/div[2]/a/h2'
    # xpath3 = './/*[@id="mitte_news"]/div[7]/div/div[1]/section/header/h3/a'

    content = driver.find_element_by_xpath('//*').text
    lst = []
    lst += re.findall(r"([-\w\s,]{3,}.)", content)
    for i in range(len(lst)):
        if i < 6:
            pass
        else:
            print(lst[i].strip())

    driver.close()
    display.stop()
    close_process("firefox")


def close_process(process):
    os.system("killall -9 " + str(process))
    print("Process killed")


def show_top():
    """show cpu most consuming processes"""
    print("This processes are using the cpu the most:")
    print(os.system("ps axo %cpu,pid,euser,cmd | sort -nr | head -n 5"))


def _3264():
    """architecture"""
    show_32_or_64_bit()


def show_32_or_64_bit():
    import platform
    print(platform.architecture()[0])


def show_mouse_position():
    # import the module
    from pymouse import PyMouse
    m = PyMouse()
    m.move(200, 200)

    # click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
    m.click(500, 300, 1)

    # get the screen size
    m.screen_size()
    # (1024, 768)

    # get the mouse position
    m.position()
    # (500, 300)


def install_xlib():
    # todo
    sudo_password = input("sudo password: ")
    command = 'sudo -H pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/'
    os.system('echo %s|sudo -S %s' % (sudo_password, command))


def percent(i: int, n: int) -> str:
    result = i / n * 100.0
    # print two digits after comma
    result = format(result, '.2f')
    return result


if __name__ == "__main__":
    cmd = str(sys.argv[1]) + "()"
    eval(cmd)
