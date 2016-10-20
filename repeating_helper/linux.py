# coding=utf-8

import os

import f


def update_system():
    path = "/home/kame/Dropbox/data/linux_update_date.txt"
    start_time = f.file_get_last_line(path)
    if f.time_diff_in_seconds(start_time, f.get_datetime()) > 3 * 3600:
        # append date to log-file
        f.file_insert_line(path, f.file_count_lines(path), f.get_datetime() + "\n")

        sudo_password = input("password:")

        print('sudo dpkg --configure -a')
        command = 'sudo dpkg --configure -a'  # repair the system
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get update -y')
        command = 'sudo apt-get update'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get upgrade -y')
        command = 'sudo apt-get upgrade -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get dist-upgrade -y')
        command = 'sudo apt-get dist-upgrade -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get autoremove -y')
        command = 'sudo apt-get autoremove -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get clean -y')
        command = 'sudo apt-get clean -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        print('sudo apt-get autoclean -y')
        command = 'sudo apt-get autoclean -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        # install pip
        command = 'sudo easy_install pip'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        # python-modules
        print('install modules with pip')
        # pil --> pillow
        # winsound --> not found
        command = 'sudo apt-get install python3-pip -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))
        import pip
        installed_packages = pip.get_installed_distributions()
        flat_installed_packages = [package.project_name for package in installed_packages]
        packages = ['numpy', 'Pillow', 'pymouse', 'pymysql', 'pyvirtualdisplay', 'requests',
                    'robotframework', 'robotframework-selenium2library',
                    'selenium', 'sympy']
        for package in packages:
            if package in flat_installed_packages:
                print(str(package) + ' already installed')
            else:
                print('Install package \'' + str(package) + '\'')
                command = 'pip install ' + str(package)
                os.system('echo %s|sudo -H -S %s' % (sudo_password, command))

        # programs
        print('install programs with apt-get')
        # pdfsam merges pdf-files
        # virtualbox-guest-dkms sind viele sinnvolle Erweiterungen für die virtualbox
        # gedit --> mousepad (leichter)
        # python-pip (war zu alt) --> easy_install pip
        # rausgenommen aber gut: flightgear, monodevelop (C# programming)
        # at first ttf-mscorefonts-installer installieren
        command = 'sudo apt-get install ' + str('ttf-mscorefonts-installer') + ' -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        programs = ['anki', 'bum', 'chromium-browser', 'chromium-codexs-ffmpeg',
                    'conky', 'ding', 'filezilla', 'firefox',
                    'flashplugin-installer', 'flightgear', 'git',
                    'gparted', 'ipython',
                    'nautilus-dropbox', 'mkgmap', 'mousepad', 'mypaint',
                    'nmap', 'pdfsam', 'preload',
                    'rhythmbox', 'skype', 'stellarium', 'subversion', 'tar',
                    'thunderbird', 'tmux', 'tuxpaint', 'vlc', 'vim',
                    'vim-runtime', 'virtualbox', 'virtualbox-guest-dkms',
                    'wine', 'wireshark', 'xchat', 'xvfb']

        for program in programs:
            command = 'sudo apt-get install ' + str(program) + ' -y'
            os.system('echo %s|sudo -S %s' % (sudo_password, command))

        # pycharm
        command = 'sudo add-apt-repository ppa:mystic-mirage/pycharm -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))
        command = 'sudo apt-get update'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))
        command = 'sudo apt-get install pycharm-community -y'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        # xlib
        command = 'sudo -H pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/'
        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        #    print('remove some programs with apt-get')
        #    programs2 = ['amarok', 'audacious', 'bfgminer', 'calibre',
        #                 'clementine', 'cowsay', 'geany',
        #	              'gpodder', 'kdiff3', 'liferea', 'lmms',
        #                 'lynx', 'meld', 'midori', 'mines', 'openbve',
        #                 'rosegarden', 'simutrans', 'sudoku', 'supertuxkart']
        #    for program in programs2:
        #        command = 'sudo apt-get remove ' + str(program)
        #        os.system('echo %s|sudo -S %s' % (sudo_password, command))

        # empty trash
        os.system('rm -rf ~/.local/share/Trash/*')


# if script is called directly
if __name__ == '__main__':
    update_system()
