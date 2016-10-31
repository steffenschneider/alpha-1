# coding=utf-8

import datetime
import inspect
import math
import os
import random
import re
import socket
import string
import struct
import subprocess
import sys
import time
import urllib
import webbrowser
from time import gmtime, strftime, localtime

import easygui
from selenium import webdriver

#############################################################

if os.name == 'nt':  # Windows
    import winsound


# todo
# refactor old files
# matplotlib

class Bcolors:
    red = '\033[91m'
    FAIL = '\033[91m'

    green = '\033[92m'
    PASS = '\033[92m'

    yellow = '\033[93m'
    WARN = '\033[93m'
    WARNING = '\033[93m'

    blue = '\033[94m'

    purple = '\033[95m'
    magenta = '\033[95m'
    HEADER = '\033[95m'

    cyan = '\033[96m'

    ENDC = '\033[0m'  # finish color
    BOLD = '\033[1m'  # no color
    UNDERLINE = '\033[4m'  # underline


class Pathes:
    custom_report = r"E:\ME\USER\Steffen\rms_files\report\custom_report.html"
    wkhtmltopdf = r"C:/Program Files/wkhtmltopdf/bin"
    path_f_py = r"/home/kame/Dropbox/code/python/f.py"
    # dropbox_path = "/home/kame/Dropbox/code/python/f.py"
    # dropbox_path = "C:/users/steffen.schneider/Dropbox/code/python/f.py"
    main_lex = r"/home/kame/Dropbox/main-lex.txt"
    main_lex_work = r"/home/kame/Dropbox/main-lex-work.txt"
    diary = r"/home/kame/Desktop/main/diary.txt"
    testfile = r"/home/kame/Desktop/testfile.txt"

##########
##########
# START
##########
##########
def battery():
    get_battery_status_in_percent()


def binary_to_string(binary_string):
    result = binary_string.decode('UTF-8')
    return result


def change_dir(path):
    os.chdir(path)


def check_if_odd(n):
    return n % 2 == 1


def check_if_root():
    if os.geteuid() == 0:
        return True
    else:
        return False


def check_sleeping_time():
    hour = int(strftime("%H", localtime()))
    if hour >= 22:
        print("It's late! Shut down your computer!!!!!")


def check_wlan():
    url = "http://www.google.de"
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        return False
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        return False
    else:
        # everything is fine
        return True


def cli_progress(actual_val, end_val, bar_length=20):
    percent = float(actual_val) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = '-' * (bar_length - len(hashes))
    print("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))


def close_process(process):
    os.system("killall -9 " + str(process))
    print("Process killed")


def com_port_read():
    import serial
    with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
        x = ser.read()  # read one byte
        s = ser.read(10)  # read up to ten bytes (timeout)
        line = ser.readline()  # read a '\n' terminated line


def com_port_write():
    import serial
    ser = serial.Serial('/dev/ttyUSB0')  # open serial port
    print(ser.name)  # check which port was really used
    ser.write(b'hello')  # write a string
    ser.close()  # close port


def count_functions_in_fpy():
    import re
    dropbox_path = get_dropbox_home()
    lst = []
    # works under linux
    for line in open(os.path.join(dropbox_path, 'code', 'python', 'f.py')):
        # count the word def in this file
        # don't count the word def in this function more than once
        lst += re.findall(r'def ([a-z]){3,}', line)
    print(str(len(lst)) + " functions available in f.py")


def create_dir_if_not_exists(directory):
    if not is_dir_available(directory):
        os.makedirs(directory)


def datetime_to_seconds(mydate):
    result = re.match(r"\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d", mydate)
    if result is not None:
        d = datetime.strptime(mydate, "%d.%m.%Y %H:%M:%S")
        result = time.mktime(d.timetuple())
        return result
    result = re.match(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d.\d\d\d", mydate)
    if result is not None:
        d = datetime.strptime(mydate, "%Y-%m-%d %H:%M:%S.%f")
        result = time.mktime(d.timetuple())
        return result
    result = re.match(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d", mydate)
    if result is not None:
        d = datetime.strptime(mydate, "%Y-%m-%d %H:%M:%S")
        result = time.mktime(d.timetuple())
        return result


def delete_chrome_history():
    # SQLite3 database
    # /home/kame/.config/chromium/Default/History
    raise Exception("Not implemented yet")


def delete_duplicates_in_list(lst):
    result = list(set(lst))
    return result


def detect_devices():
    import subprocess
    df = subprocess.check_output("lsusb", shell=True)
    devices = []
    for i in df.decode('UTF-8').split('\n'):
        devices.append(i)
    return devices


def download_mp3_to_dropbox(url):
    import urllib

    # url = "http://podcast-mp3.dradio.de/podcast/2016/03/07/dlf_20160307_1949_c03fc129.mp3"
    dropbox_path = get_dropbox_home()
    path = dropbox_path + "/new_podcasts/"
    urllib.request.urlretrieve(url, path + str(url[-30:]))


def file_count_lines(path):
    with open(path, 'r') as fin:
        a = fin.readlines()
    return len(a)


def file_delete_duplicate_lines(path):
    lst = file_to_list(path)
    lst_2 = delete_duplicates_in_list(lst)
    list_to_file(path, lst_2)


def file_delete_empty_lines(file_in):
    with open(file_in, 'r') as fin:
        data = ("".join(line for line in fin if not line.isspace()))
    with open(file_in, 'w') as fout:
        fout.writelines(data)


def file_delete_first_line(file_in):
    with open(file_in, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file_in, 'w') as fout:
        fout.writelines(data[1:])


def file_delete_lines_with_entry(file_in, entry):
    f = open(file_in, "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if entry in i:
            pass
        else:
            f.write(i)
    f.truncate()
    f.close()


def file_get_last_line(file_):
    myarr = []
    file_input = open(file_)
    text = file_input.readlines()  # .read() reads only one line
    for line in text:
        myarr.append(line)
    return myarr[-1:][0][:-1]


def file_get_string(path):
    mystring = ""
    with open(path) as f:
        contents = f.readlines()
    for elem in contents:
        mystring += str(elem)
    return mystring


def file_get_text_from_file(path):
    myarr = []
    file_input = open(path)
    text = file_input.readlines()  # .read() reads only one line
    for line in text:
        myarr.append(line)
    return myarr


def file_insert_line(path, index, value):
    f = open(path, "r+")
    data = f.readlines()
    data.insert(index, value)
    f.seek(0)
    data = "".join(data)
    f.write(data)
    f.truncate()
    f.close()


def file_replace_words(file_in, word_to_replace, replace_with):
    f = open(file_in, "r+")
    data = f.readlines()
    f.seek(0)
    for line in data:
        line = re.sub(word_to_replace, replace_with, line)
        f.write(line)
    f.truncate()
    f.close()


def file_sort_lines(path):
    lst = file_to_list(path)
    sorted_list = sorted(lst)
    list_to_file(path, sorted_list)
    

def file_to_list(path):
    with open(path) as f:
        contents = f.readlines()
    return contents


def file_word_analysis(path):
    from collections import Counter
    file = open(path, "r")
    lines = file.readlines()
    words = [word.lower() for line in lines for word in line.split()]
    list2 = []
    for word in words:
        word = re.sub("\.", "", word)
        word = re.sub("-", "", word)
        word = re.sub("\(", "", word)
        word = re.sub("\)", "", word)
        word = re.sub("\?", "", word)
        word = re.sub("\!", "", word)
        word = re.sub("#", "", word)
        word = re.sub("\[", "", word)
        word = re.sub("\]", "", word)
        word = re.sub(",", "", word)
        word = re.sub("\"", "", word)
        word = re.sub("\'", "", word)
        word = re.sub(":", "", word)
        word = re.sub(";", "", word)
        word = re.sub("\/", " ", word)
        list2.append(word)
    wordcount = Counter(list2)
    for item in sorted(wordcount.items(), key=lambda l: l[1], reverse=True): print("{}\t{}".format(*item))


def get_battery_status_in_percent():
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
    # print("battery: " + result + " %")
    if float(result) < 20.0:
        print("###########################################")
        print("###########################################")
        print("#########      low - battery      #########")
        print("###########################################")
        print("###########################################")
    return result


def get_computer_name():
    print("Computer name: " + str(socket.gethostname()))


def get_current_path():
    result = os.getcwd()
    return result


def get_date():
    date = strftime("%d.%m.%Y", localtime())  # local time
    return date


def get_datetime():
    datetime_ = strftime("%d.%m.%Y %H:%M:%S", localtime())  # local time
    return datetime_


def get_datetime_plus_two_minutes():
    ts = get_seconds_since_1970_with_microseconds()
    ts2 = ts + 120
    datetime_ = strftime('%Y-%m-%d %H:%M:%S', localtime(ts2))
    return datetime_


def get_day_of_the_year():
    result = datetime.datetime.now().timetuple().tm_yday
    # print(result)
    return result


def get_dropbox_home():
    from platform import system
    import base64
    import os.path
    _system = system()
    if _system in ('Windows', 'cli'):
        host_db_path = os.path.join(get_local_appdata_path(),
                                    'Dropbox',
                                    'host.db')
    elif _system in ('Linux', 'Darwin'):
        host_db_path = os.path.expanduser('~'
                                          '/.dropbox'
                                          '/host.db')
    else:
        raise RuntimeError('Unknown system={}'
                           .format(_system))
    if not os.path.exists(host_db_path):
        raise RuntimeError("Config path={} doesn't exists"
                           .format(host_db_path))
    with open(host_db_path, 'r') as f:
        data = f.read().split()

    return base64.b64decode(data[1]).decode('ascii')


def get_filenames_from_dir(path):
    import glob
    path += "*.mp3"
    return glob.glob(path)


def get_id_tags(url):
    # check link syntax
    if url[:4] != 'http' and url[:3] != 'www':
        url = 'http://www.' + str(url)
    if url[:4] != 'http':
        url = 'http://' + str(url)
    if url[-1:] != '/':
        url += '/'

    # get content
    content_ = urllib.request.urlopen(url).read()
    items = re.findall(r'id=\"(.*?)\"', str(content_))
    return items


def get_installed_modules():
    import pip
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s" % i.key for i in installed_packages])
    return installed_packages_list


def get_links(url):
    # example link
    # url = 'http://www.heise.de/'

    # check link syntax
    if url[:4] != 'http' and url[:3] != 'www':
        url = 'http://www.' + str(url)
    if url[:4] != 'http':
        url = 'http://' + str(url)
    if url[-1:] != '/':
        url += '/'

    # get content
    content_ = urllib.request.urlopen(url).read()

    # search for "a href"
    items = re.findall("<a href=\"(.+\.html)\"", content_)  # get links with ending .html

    # delete duplicates
    lst = list(set(list(items)))

    # return links
    for i in range(len(lst)):
        if lst[i][:4] != 'http':
            lst[i] = url + str(lst[i][1:])

    return lst


def get_local_appdata_path():
    path = os.getenv('LOCALAPPDATA')
    return path


def get_local_time():
    time_now = strftime("%H:%M:%S", localtime())  # local time
    return time_now


def get_mac():
    from uuid import getnode as get_mac_
    mac = get_mac_()
    return mac


def get_minute_of_the_day():
    hour = strftime("%H", localtime())
    minute = strftime("%M", localtime())
    minute_of_the_day = int(hour) * 60 + int(minute)
    return str(minute_of_the_day)


def get_mod():
    result = get_minute_of_the_day()
    return result


def get_mousepos():
    curr = subprocess.check_output(["xdotool", "getmouselocation"]).decode("utf-8")
    return [int(it.split(":")[1]) for it in curr.split()[:2]]


def get_my_ip():
    # myip = socket.gethostbyname(socket.gethostname())
    if get_my_os() == 'linux':
        myip = os.system("ifconfig | awk '/inet addr/{print substr($2,6)}'")
        myip_deutsch = os.system("ifconfig | awk '/inet Adresse:/{print substr($3,7)}'")
        if len(str(myip)) < 2:
            print(myip_deutsch)
        else:
            print(myip)
        return myip
    else:
        hostname = socket.gethostname()
        myip = socket.gethostbyname(hostname)
        print(myip)
        return myip
        # or
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8", 80))
        # return s.getsockname()[0]


def get_my_os():
    get_os_name()


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


def get_os_name():
    """ e.g. posix, nt """
    result = os.name
    if result == 'posix':
        return 'linux'
    elif result == 'nt':
        return 'windows'
    else:
        return 'unknown system'


def get_python_version():
    print(sys.version)


def get_script_path():
    result = os.path.dirname(os.path.abspath(__file__))
    return result


def get_second():
    time_now = strftime("%S", localtime())
    return time_now


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


def get_temperature():
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


def get_time():
    time_ = get_local_time()
    return time_


def get_top():
    """show cpu most consuming processes"""
    print("This processes are using the cpu the most:")
    print(os.system("ps axo %cpu,pid,euser,cmd | sort -nr | head -n 5"))


def get_utc_time():
    time_now = strftime("%H:%M:%S", gmtime())  # utc
    return time_now


def get_weekday():
    """
    0 --> Monday
    6 --> Sunday
    I will add 1
    1 --> Monday
    7 --> Sunday
    """
    result = datetime.datetime.today().weekday() + 1
    return result


def html_analyse_element(self, xpath):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    elements = self._driver.find_elements_by_xpath(xpath)
    print("innerHTML of xpath: " + Bcolors.blue + str(xpath) + Bcolors.ENDC)
    for element in elements:
        print(element.get_attribute('innerHTML'))
    print("outerHTML of xpath: " + Bcolors.blue + str(xpath) + Bcolors.ENDC)
    for element in elements:
        print(element.get_attribute('outerHTML'))
    print("text of xpath: " + Bcolors.blue + str(xpath) + Bcolors.ENDC)
    for element in elements:
        print(element.text)
    print("\n")


def html_open_random_bookmarks_chromium(n=5):
    file_ = "/home/kame/.config/chromium/Default/Bookmarks"

    file_input = open(file_, "r")
    text = file_input.readlines()  # .read() read only one line
    count = 0
    for line in text:
        if '"url":' in line:
            count += 1

    for i in range(n):
        # choose random bookmark
        rnd = random.randint(0, count - 1)
        count = 0
        line_with_link = ""
        for line in text:
            if '"url":' in line:
                if count == rnd:
                    line_with_link = line
                count += 1

        # todo - sometimes not working
        url = re.findall(r"url.*\"(.*)\"", line_with_link)[0]
        webbrowser.open(url, new=2)  # open in a new tab, if possible


def html_to_pdf(input_file, output_file):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    if "\\" in output_file:
        pass
    else:
        output_file = r"C:\Users\Steffen.schneider\Desktop\\" + str(output_file)
    get_os_name()
    path = Pathes.wkhtmltopdf
    assert os.path.exists(path), "wkhtmltopdf doesn't exist. Please install"
    change_dir(path)
    get_current_path()
    os.system("wkhtmltopdf " + str(input_file) + " " + str(output_file))


def install_easygui():
    # windows
    if os.name == 'nt':
        os.system("py -2 -m pip install easygui --trusted-host pypi.python.org")
        os.system("py -3 -m pip install easygui --trusted-host pypi.python.org")
    if os.name == 'posix':
        sudo_password = input("sudo password: ")
        command = 'sudo -H pip install easygui'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))


def install_ipython():
    print("You have to set the correct python path")
    print(r"set PATH = % PATH %; C:\Users\steffen.schneider\AppData\Local\Programs\Python\Python35-32\Scripts")
    os.system("py -3 -m pip install ipython --trusted-host pypi.python.org")


def install_numpy():
    if python_32_or_64_bit() == '32':
        print("download from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy")
        print("pip install xxxxx.whl")
    elif python_32_or_64_bit() == '64':
        os.system("py -2 -m pip install numpy --trusted-host pypi.python.org")
        os.system("py -3 -m pip install numpy --trusted-host pypi.python.org")
    else:
        print("python_32_or_64_bit() isn't working correct")

def install_pcap():
    os.system("py -2 -m pip install pypcap --trusted-host pypi.python.org")


def install_pdfminer():
    os.system("py -3 -m pip install pdfminer3k --trusted-host pypi.python.org")


def install_pillow():
    os.system("py -2 -m pip install pillow --trusted-host pypi.python.org")
    os.system("py -3 -m pip install pillow --trusted-host pypi.python.org")


def install_pymysql():
    os.system("py -2 -m pip install pymysql --trusted-host pypi.python.org")
    os.system("py -3 -m pip install pymysql --trusted-host pypi.python.org")


def install_scapy():
    os.system("py -2 -m pip install scapy --trusted-host pypi.python.org")
    os.system("py -3 -m pip install scapy-python3 --trusted-host pypi.python.org")


def install_scipy():
    os.system("easy_install scipy")
    # os.system("py -3 -m pip install scipy --trusted-host pypi.python.org")


def install_selenium():
    os.system("py -2 -m pip install selenium --trusted-host pypi.python.org")
    os.system("py -3 -m pip install selenium --trusted-host pypi.python.org")


def install_tkinter():
    raise NotImplementedError
    # Linux:
    # sagi tkinter-tk
    # sagi tkinter3-tk
    # Windows:
    # wird bei der Pythoninstallation wahlweise hinzugefügt

def install_win32gui():
    print("First download from here --> https://sourceforge.net/projects/pywin32/files/pywin32")
    print("You need a " + str(python_32_or_64_bit()) + " bit version")


def install_xlib():
    if os.name == 'posix':
        sudo_password = input("sudo password: ")
        command = 'sudo -H pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))
    else:
        raise Exception("not implemented for windows yet")


def is_dir_available(path):
    import os
    result = os.path.isdir(path)
    return result


def is_dir_existing(path):
    is_dir_available(path)


def is_file_available(path):
    import os
    result = os.path.exists(path)
    return result


def is_root():
    if os.geteuid() == 0:
        return True
    else:
        return False


def is_some_number(mystring):
    # print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- "
    # + inspect.stack()[0][3] + "()" + Bcolors.ENDC)
    """
    Is mystring int of float (with . or , separator)?
    :param mystring: int or str
    :return: bool
    """
    mystring = str(mystring)
    mystring = re.sub(",", ".", mystring)
    try:
        if float(mystring):
            return True
    except ValueError:
        return False


def list_add_headline(mylist, header):
    elements = header.split("\t")
    line = []
    for elem in elements:
        line.append(elem)
    mylist.insert(0, line)
    return mylist


def list_delete_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers


def list_to_file(path, mylist):
    f = open(path, "w")
    f.write(''.join(str(x) for x in mylist))
    f.close()


def list_to_tab_delimited_string(mylist):
    result = ('\t'.join(i) for i in mylist)
    return result


def mod():
    get_mod()


def mouse_click():
    os.system("xte 'mouseclick 1'")


def my_ip():
    return get_my_ip()


def nm_to_ev(lambda_):
    """
    Convert the wavelength in nm to eV

    Parameters
    ----------
    lambda_

    Returns
    -------
    voltage in eV
    """
    h = 6.2 * 10 ** -34  # (?)
    c = 299792458
    f = c / lambda_
    e = h * f * 100000000  # because of nm instead of m
    e2 = 1.0 * e / (10 ** -19)
    print(e2, "eV")
    return e2


def open_computer():
    open_computer_und_kommunikation()


def open_computer_und_kommunikation():
    import webbrowser
    url = "http://www.deutschlandfunk.de/podcast-computer-und-kommunikation-komplette-sendung.416.de.podcast.xml"
    new = 2  # open in a new tab, if possible
    webbrowser.open(url, new=new)


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


def os_32_or_64_bit():
    import platform
    print("OS: " + str(platform.machine()[-2:]) + " bit")
    return platform.machine()[-2:]


def pass_fail_stats_fom_outputxml():
    if "f.py" in inspect.stack()[0][1]:
        pass
    else:
        print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
            3] + "()" + Bcolors.ENDC)
    file_ = r"E:/ME/USER/Steffen/rms_files/report/output.xml"
    for i in range(100000):
        print("\n\n")
        myarr = file_get_text_from_file(file_)
        passcount = 0
        failcount = 0
        starttime = re.findall('\d\d:\d\d:\d\d', myarr[1])[0]
        starttime = time_to_seconds(starttime)
        timenow = time_now_to_seconds()
        timediff = timenow - starttime
        expected_duration = 115 * 60
        done = timediff * 1.0 / expected_duration * 100.0
        for element in myarr:
            if 'critical="yes"' in element:
                if 'status="PASS"' in element:
                    passcount += 1
                if 'status="FAIL"' in element:
                    print(element)
                    failcount += 1
            if '<test' in element:
                element = re.findall('name=\"(.*)\"', element)[0]
                print(element)
        sum_ = passcount + failcount + 0.000001  # wg. division 0
        percent_ = passcount * 100.0 / sum_
        arg1 = ""
        if percent_ > 99.0:
            arg1 = "+++++++++++++++++++++++++++++++++++++"
        print(" Pass: %s    Fail: %s    Percent_pass: %s    Duration: %s    Done: %s    %s" % (
            passcount, failcount, format(percent_, '.2f'), format(timediff * 1.0 / 60, '.1f'), format(done, '.1f'),
            arg1))
        time.sleep(20)


def pdf_to_csv(filename, separator, threshold):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    # the separator to use with the CSV
    separator = ';'
    # the distance multiplier after which a character is considered part of a new word/column/block.
    # Usually 1.5 works quite well
    threshold = 1.5
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    from pdfminer.converter import LTChar, TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfpage import PDFPage

    class CsvConverter(TextConverter):
        def __init__(self, *args, **kwargs):
            TextConverter.__init__(self, *args, **kwargs)
            self.separator = separator
            self.threshold = threshold

        def end_page(self, n):
            from collections import defaultdict
            lines = defaultdict(lambda: {})
            for child in self.cur_item._objs:  # <-- changed
                if isinstance(child, LTChar):
                    (_, _, x, y) = child.bbox
                    line = lines[int(-y)]
                    line[x] = child._text.encode(self.codec)  # <-- changed
            for y in sorted(lines.keys()):
                line = lines[y]
                self.line_creator(line)
                self.outfp.write(self.line_creator(line))
                self.outfp.write("\n")

        def line_creator(self, line):
            keys = sorted(line.keys())
            # calculate the average distange between each character on this row
            average_distance = sum([keys[j] - keys[j - 1] for j in range(1, len(keys))]) / len(keys)
            # append the first character to the result
            result = [line[keys[0]]]
            for k in range(1, len(keys)):
                # if the distance between this character and the last character is greater than the average*threshold
                if (keys[k] - keys[k - 1]) > average_distance * self.threshold:
                    # append the separator into that position
                    result.append(self.separator)
                # append the character
                result.append(line[keys[k]])
            printable_line = ''.join(result)
            return printable_line

    # ... the following part of the code is a remix of the
    # convert() function in the pdfminer/tools/pdf2text module
    rsrc = PDFResourceManager()
    outfp = StringIO()
    device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
    # because my test documents are utf-8 (note: utf-8 is the default codec)

    print("open file")
    fp = open(filename, 'rb')

    interpreter = PDFPageInterpreter(rsrc, device)
    print("for-loop")
    for i, page in enumerate(PDFPage.get_pages(fp)):
        outfp.write("START PAGE %d\n" % i)
        if page is not None:
            # print('page exist')
            interpreter.process_page(page)
        outfp.write("END PAGE %d\n" % i)

    device.close()
    fp.close()

    return outfp.getvalue()


def percent_of_the_day():
    result = 100 * float(get_mod()) / 1440.0
    result = two_digits_after_point(result)
    return result


def play_sound_under_windows():
    freq = 444
    dur = 111
    winsound.Beep(freq, dur)
    freq = 333
    dur = 222
    winsound.Beep(freq, dur)
    freq = 444
    dur = 111
    winsound.Beep(freq, dur)


def print_child_nodes(self, xpath):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    print("Child nodes of xpath: " + Bcolors.blue + str(xpath) + Bcolors.ENDC)
    children = self._driver.find_elements_by_xpath(str(xpath) + '/*')
    for child in children:
        # print("<%s> %r" % (child.tag_name, child.text[:60]))
        print_child_nodes(self, str(xpath) + '/' + str(child.tag_name))


def python_32_or_64_bit():
    bit = struct.calcsize("P") * 8
    # alternative
    # import ctypes
    # print(ctypes.sizeof(ctypes.c_voidp) * 8)
    # import platform
    # print(platform.architecture()[0])
    return str(bit)


def random_string():
    list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
             'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z',
             '_', '!']

    list2 = []
    n_zeichen = len(list_)
    laenge = 80
    for i in range(laenge):
        x = int(random.randint(0, n_zeichen - 1))
        list2.append(list_[x])

    z = str(''.join(str(i) for i in list2))
    print(z)
    print(re.sub("(..........)", "\\1\n", z))  # Breite entspricht Anzahl der Punkte
    return z


def random_string_2(n):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    result = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))
    print(result)
    return result


def relais_gateway():
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    server_name = b"10.65.100.20"
    server_port = 2101
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_name, server_port))

    message = b"{ 99TST29;1;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)

    time.sleep(1)

    message = b"{ 99TST29;0;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)


def relais_lanlogger():
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)

    server_name = b"10.65.100.25"
    server_port = 2101
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_name, server_port))

    message = b"{ 99TST29;1;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)

    time.sleep(1)

    message = b"{ 99TST29;0;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)


def relais_minilogger():
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)

    server_name = b"10.65.100.20"
    server_port = 2101
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_name, server_port))

    message = b"{ 99TST30;1;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)

    time.sleep(1)

    message = b"{ 99TST30;0;}\r"
    s.send(message)
    data = s.recv(2048)
    print(data)


def rgbint_to_rgbtuple(rgbint):
    red = rgbint & 255
    green = (rgbint >> 8) & 255
    blue = (rgbint >> 16) & 255
    return red, green, blue


def rotronic_analyse_sync():
    file_ = r"E:\ME\Gemeinsame_Daten\10000.Project\11045.Projekt w konzept\35_Validation\Systemtest\log_files\putty.txt"
    file_input = open(file_, "r")
    text = file_input.readlines()
    # extract time slot number and time of all lines with string 'Sync'
    pattern_1 = r"@ (.*),"
    pattern_2 = r"Sync: (.*)"
    for line in text:
        if 'Sync' in line:
            string_ = line[:-1]
            number = re.findall(pattern_1, string_)[0]
            time_ = re.findall(pattern_2, string_)[0]
            print(str(number) + "\t" + str(time_))


def search_all_files_for_string(mystring):
    import glob
    path = r"C:\Users\steffen.schneider\Desktop\RMS\**"

    with open(r"C:/Users/steffen.schneider/Desktop/search.txt", "w") as f:
        for filename in glob.iglob(path, recursive=True):
            # if name.endswith((".html", ".htm", ".txt", ".vb")):
            try:
                with open(filename) as currentFile:
                    text = currentFile.read()
                    if mystring in text:
                        f.write('Found string in ' + filename + '\n')
                    else:
                        pass
                        # f.write('NOT ' + filename + '\n')
            except RuntimeError:
                pass


def search_file_in_path_and_subfolders(filename, path):
    import os
    # path = "C:/Users/steffen.schneider"
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(filename):
                # if file.endswith(".dropbox"):
                print(os.path.join(root, file))


def set_position(x, y):
    os.system("xte 'mousemove " + str(x) + " " + str(y) + "'")


def show_all_functions_in_folder(path):
    # path = r"C:\Users\steffen.schneider\Desktop\RMS"
    import glob
    path = str(path) + "\**"

    # with open(r"C:/Users/steffen.schneider/Desktop/search.txt", "w") as f:
    for filename in glob.iglob(path, recursive=True):
        if filename.endswith((".html", ".htm", ".txt", ".vb", ".aspx")):
            print("####################################################")
            print(filename)
            try:
                counter = 0

                with open(filename) as currentFile:
                    for i in range(11111):  # todo
                        text = currentFile.readline()
                        if len(text) < 300:
                            if " Function " in text:
                                # f.write('Found string in ' + filename + '\n')
                                print("line: " + str(counter) + "\t" + text[:-2])
                            else:
                                pass
                                # f.write('NOT ' + filename + '\n')
                        counter += 1
            except RuntimeError:
                pass


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


def sniffer(host):
    # host to listen on
    if host == "":
        host = my_ip()

    # create a raw socket and bind it to the public interface
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer_ = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer_.bind((host, 0))

    # we want the IP headers included in the capture
    sniffer_.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # if we’re using Windows, we need to send an IOCTL
    # to set up promiscuous mode
    if os.name == "nt":
        sniffer_.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # read in packets
    for i in range(10):
        print(sniffer_.recvfrom(65565))

    # if we’re using Windows, turn off promiscuous mode
    if os.name == "nt":
        sniffer_.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


def sort_f_py():
    path = Pathes.path_f_py

    list_a = file_to_list(path)
    start_sequence = ["##########\n", "##########\n", "# START\n", "##########\n", "##########\n"]
    end_sequence = ["##########\n", "##########\n", "# END\n", "##########\n", "##########\n"]

    # search start + end
    start_pos = [(i, i + len(start_sequence)) for i in range(len(list_a)) if
                 list_a[i:i + len(start_sequence)] == start_sequence]
    start_pos = start_pos[0][1]
    end_pos = [(i, i + len(end_sequence)) for i in range(len(list_a)) if
               list_a[i:i + len(end_sequence)] == end_sequence]
    end_pos = end_pos[0][0]

    list_start = list_a[0:start_pos]
    list_to_sort = list_a[start_pos:end_pos]
    list_end = list_a[end_pos:]

    # create 2d-list
    lst = []
    row = -1
    n_functions = 0
    for line in list_to_sort:
        if line[:3] == 'def':
            n_functions += 1

    # create output array rows
    for i in range(n_functions):
        lst.append([])

    # every functions goes in one list-row
    start_flag = 0
    for line in list_to_sort:
        if line == "\n" and start_flag == 0:
            pass
        else:
            if line != "\n":
                start_flag = 1
            if line[:3] == 'def':
                row += 1
            lst[row].append(line)

    # sort
    two_dim_list = sorted(lst, key=lambda x: x[0].lower())

    flat = [x for sublist in two_dim_list for x in sublist]
    output_list = list_start + flat + list_end
    list_to_file(path, output_list)


def sort_functions_alphabetically(filename):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    """
    Alpha-state!
    Use with care!
    Doesn't work if property is available before def keyword!!!!
    A few times this function doesn't work correctly!

    :param filename:
    :return:
    """
    """
    input:

    class Abc:
        def b():
            b1
            b2

        def a():
            a1
            a2

    output:

    class Abc:
        def a():
            a1
            a2

        def b():
            b1
            b2
    """

    # import file
    mylist = []
    file_input = open(filename)
    text = file_input.readlines()
    for line in text:
        mylist.append(line)

    # append "\n" in last line of my list
    mylist.append("\n")

    helparray = []
    row = -1
    flag_first_def_found = 0
    # only take def lines and remember start
    # and end of each def in a help array
    print("len of the input: " + str(len(mylist)))
    for i in range(len(mylist)):
        # fixme, copy code from sort f.py
        if 'def' in mylist[i]:
            flag_first_def_found = 1
            row += 1
            helparray.append([])
            helparray[row].append(mylist[i])
        if flag_first_def_found == 1:
            helparray[row].append(i)

    # sort def lines --> first column
    helparray = sorted(helparray, key=lambda l: l[0])
    # print(helparray)

    # create output array
    output_array = []
    for n in range(len(mylist)):
        output_array.append([])

    # copy the first part of the file before the main_2_functions begin
    # find first function
    first_def_line = None
    for k in range(len(mylist)):
        if 'def' in mylist[k]:
            first_def_line = k
            break
    # copy
    for m in range(0, first_def_line + 1 - 1):
        output_array[m] = mylist[m]

    # copy every function (def)
    output_array_counter = first_def_line
    for s in range(len(helparray)):
        def_start = helparray[s][1]
        def_end = helparray[s][-1]
        for j in range(def_start, def_end + 1):
            output_array[output_array_counter] = mylist[j]
            output_array_counter += 1

    # write file
    with open(filename, "w") as myfile:
        for d in range(len(output_array)):
            myfile.write(str(output_array[d]))


def sound_beepequivalent_under_linux():
    import subprocess
    subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'bell'])


def stack_overflow_python_documentation_random_topic():
    rnd = random.randint(1, 8)
    url = r"http://stackoverflow.com/documentation/python/topics?page=" + str(rnd) + "&tab=popular"
    content_ = urllib.request.urlopen(url).read().decode('UTF-8')
    items = re.findall("data-topic-url=\"(.*)\">", content_)  # get links with ending .html
    item_url = random.choice(items)
    new = 2  # open in a new tab, if possible
    webbrowser.open(item_url, new=new)


def string_to_file(path, mystring):
    f = open(path, "w")
    f.write(''.join(str(x) for x in mystring))


def system_info():
    get_computer_name()
    os_32_or_64_bit()
    python_32_or_64_bit()
    get_python_version()
    count_functions_in_fpy()


def test_1():
    assert (1 == 1)
    assert (1 != 2)
    assert isinstance('abc', str)
    assert isinstance(1, int)
    assert isinstance(2.34, float)
    assert not isinstance(123, str), "type is string but shouldn't"
    assert (2 ** 2 == 4)
    assert (4.0 / 3 == 1.3333333333333333)
    assert isinstance(True, bool)
    assert not isinstance(True, str)
    assert isinstance('True', str)
    assert not isinstance('True', bool)
    assert (int(get_seconds_since_1970_without_microseconds()) > 111111111)
    assert (math.cos(0.5) ** 2 + math.sin(0.5) ** 2 == 1.0)
    assert True
    assert 1
    assert (int(str(1)) == 1)
    assert (bin(1) == '0b1')
    assert (int('0b1111', 2) == 15)


def test_two_digits_after_point():
    # float
    assert two_digits_after_point(1.2345) == 1.23
    assert two_digits_after_point(1.238) == 1.24
    assert two_digits_after_point(1.2) == 1.2
    # str
    assert two_digits_after_point("1.2345") == "1.23"
    assert two_digits_after_point("1.238") == "1.24"
    assert two_digits_after_point("1.2") == "1.20"
    assert two_digits_after_point("1") == "1.00"
    assert two_digits_after_point("-1") == "-1.00"
    # int
    assert two_digits_after_point(3) == 3.00


def textbox(msg):
    print(Bcolors.cyan + re.findall(r".*\\(.*)", inspect.stack()[0][1])[0] + " --- " + inspect.stack()[0][
        3] + "()" + Bcolors.ENDC)
    """
    Displays an enterbox. The input number is equal to the waiting time after the enter press
    :param msg: Text displayed in the title
    :return: None
    """
    print(msg)
    waittime = easygui.enterbox(msg, title="easygui - type waittime")  # programm is waiting here
    if waittime == "":
        waittime = "0"
    if is_some_number(waittime):
        time.sleep(int(waittime))


def time_diff(start_time, end_time):
    from datetime import datetime
    datetime_format = '%d.%m.%Y %H:%M:%S'
    et = datetime.strptime(end_time, datetime_format)
    st = datetime.strptime(start_time, datetime_format)
    dt = et - st
    print(dt.days)
    print(dt.seconds)
    return dt


def time_diff_in_seconds(start_time, end_time):
    from datetime import datetime
    datetime_format = '%d.%m.%Y %H:%M:%S'
    et = datetime.strptime(end_time, datetime_format)
    st = datetime.strptime(start_time, datetime_format)
    dt = et - st
    result = 24 * 3600 * dt.days + dt.seconds
    return result


def time_now_to_seconds():
    time_now = get_local_time()
    time_in_seconds = time_to_seconds(time_now)
    result = time_in_seconds
    return result


def time_to_seconds(mytime):
    my_regex = re.compile("\d\d:\d\d:\d\d")
    assert my_regex.match(mytime) is not None, "time has wrong format"
    sum_ = 0
    sum_ += 3600 * int(mytime[0:2])
    sum_ += 60 * int(mytime[3:5])
    sum_ += int(mytime[6:8])
    result = sum_
    return result


def two_digits_after_point(value):
    """third, fourth etc. digit after decimal separator were removed"""
    if isinstance(value, str):
        result = format(float(value), '.2f')
        return result
    elif isinstance(value, float):
        result = format(value, '.2f')
        return float(result)
    elif isinstance(value, int):
        value = float(value)
        print(value)
        result = format(value, '.2f')
        return float(result)
    else:
        raise Exception("type " + str(type(value)) + " not implemented yet")


def upgrade_linux():
    sudo_password = input("sudo password: ")
    command = 'apt-get update'
    os.system('echo %s|sudo -S %s' % (sudo_password, command))
    command = 'apt-get upgrade -y'  # -y for typing yes
    os.system('echo %s|sudo -S %s' % (sudo_password, command))


def upgrade_pip():
    os.system("py -3 -m pip install --upgrade pip --trusted-host pypi.python.org")


def utc_to_localtime(timestring):
    from datetime import datetime, timedelta
    mytime = datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S.%f")
    delta = 1 + time.localtime().tm_isdst
    mytime += timedelta(hours=delta)
    result = mytime.strftime("%Y-%m-%d %H:%M:%S.%f")
    return result[:-3]


def watch_position():
    # os.system("xdotool getmouselocation")
    os.system("watch xdotool getmouselocation")  # watch live
    # os.system("xdotool getmouselocation 2>/dev/null | cut -d\  -f1,2 -")


##########
##########
# END
##########
##########


if __name__ == '__main__':
    rotronic_analyse_sync()
