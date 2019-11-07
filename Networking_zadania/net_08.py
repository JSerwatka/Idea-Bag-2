# Country from IP Lookup

import ipinfo
import re


def check_if_ip_correct(ip_address: str) -> bool:
    pattern_ip4 = r'[0-255].[0-255].[0-255].[0-255]'
    pattern_ip6 = r''

    if re.match(pattern_ip4, ip_address) or re.match(pattern_ip6, ip_address):
        return True
    else:
        return False


def country_from_ip_lookup():
    print("Insert your ip address:" + '\n')
    ip_address = input()
    if not check_if_ip_correct(ip_address):
        raise ValueError("Ip is incorrect")

    access_token = '12ef775d6a77db'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    print(
        "IP data for address: {} ".format(ip_address) + '\n'
        "\t" + "Country: " + details.country_name + '\n'
        "\t" + "City: " + details.city + '\n'
        "\t" + "Internet provider: " + details.org + '\n'
    )


country_from_ip_lookup()
