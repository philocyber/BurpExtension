#!/usr/bin/env python
__author__ = 'Richie Prieto'
__description__ = '''Python Decoder Tool - Kulkan Security challenge\n\n'''


import sys
import argparse
import requests
import base64


def banner():
    ascii_art = '''                    
###############################################################
###############################################################
###################################* ,,,,,,,,,,. ##############
################ . , ..,  /#### ,,,.              #############
########### *,   ,,, ,,,   *,. .  .,....,,,,,,,,,,,. ##########
##########(,,,    *,,     ,,,     ....,,,,..   ..,,,,, (#######
##########.*,    ,,.    ,      .. .    ...,,,,,,,,  ... ,######
##########  ,.  .. /         ,,,*  .,,,.,   . .,,,,,,.   ######
###########      ,@(  .. .         .,   ..,,,,    .,,,, ,######
######## **.,,      .. %@       .  ,....     .,,,... ,,, ######
#######,.       .  ..@(&( .  ,,,      .,             ... (#####
########.@        *@@/# .        .,,.,,               .. ######
#######  ///*  &&.%&  .                                 (######
########/ *.*. ***,  .          .. .              . .....######
########./*      .   .  .       ...                . .... #####
#######(*/*.**                                    *      ######
#######/.*.*,*                        . ..        (############
########*                            . ..  ..     #############
#########****                      .. . . ..     ##############
##########  ..                     . .... .     ###############
##############                    .    .       ################
#############/,,,,,,,,,.         .  ...      ##################
############# .. ,, ,              .     .#####################
############ ,.                      ##########################
############,,,,,,,,,                      ####################
############ .,,,, ,,                        ##################
#############. .                              .################
############## ,,,,,,,/                        ################
############### ,,//////                       ################

 ________        __ __     ____               _      __         
/_  __/ / ___   / //___ __/ / /_____ ____    | | /| / ___ ___ __
 / / / _ / -_) / ,< / // / /  '_/ _ `/ _ \   | |/ |/ / _ `/ // /
/_/ /_//_\__/ /_/|_|\_,_/_/_/\_\\_,_/_//_/   |__/|__/\_,_/\_, / 
                                                         /___/  
'''
    return ascii_art


finishMsg = "The decoding process has been completed"

print(banner())
print('By: {}'.format(__author__))
print(__description__)


def decoder(target_url):
    response = requests.get(target_url[0])
    # Saving the http request into jsonResponse variable
    json_response = response.json()
    # obtaining and decoding the secret value from the 'jsonResponse' dictionary
    # decode('utf-8') was used to get rid of the b' before the decoded string
    secret_value = base64.b64decode(json_response['data']).decode('utf-8')

    json_response['data'] = secret_value
    # print(f"{secret_value}\n")
    return secret_value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u ', '--url',
                        help="specify the url, like the following examples: http://example.com or https://example.com",
                        required=True)
    args = parser.parse_args()

    url = [args.url]
    # calling function and returning the decoded value
    print(f"{decoder(url)}\n")

    if args.url is None:
        print("The argument -u [URL] is invalid: The example is -u http://example.com or -u https://example.com")
        sys.exit()
