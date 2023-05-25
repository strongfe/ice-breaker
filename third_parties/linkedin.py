import os
from typing import Dict

import requests
import langchain


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information form LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    # print(f"Response Status Code: {response.status_code}")
    # print(f"Response Text: {response.text}")
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# def scrape_linkedin_profile(linkedin_profile_url: str):
#     api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
#     api_key = os.environ.get('PROXYCURL_API_KEY')
#     print(api_key)
#     header_dic = {'Authorization': 'Bearer ' + api_key}
#     params = {
#         'url': linkedin_profile_url,
#         'fallback_to_cache': 'on-error',
#         'use_cache': 'if-present',
#         'skills': 'include',
#         'inferred_salary': 'include',
#         'personal_email': 'include',
#         'personal_contact_number': 'include',
#         'twitter_profile_id': 'include',
#         'facebook_profile_id': 'include',
#         'github_profile_id': 'include',
#         'extra': 'include',
#     }
#
#     response = requests.get(api_endpoint, params=params, headers=header_dic)

# def scrape_linkedin_profile(linkedin_profile_url: str):
#     api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
#     api_key = os.environ.get('PROXYCURL_API_KEY')
#     print(api_key)
#     header_dic = {'Authorization': 'Bearer ' + api_key}
#     params = {
#         'url': linkedin_profile_url,
# 'fallback_to_cache': 'on-error',
# 'use_cache': 'if-present',
# 'skills': 'include',
# 'inferred_salary': 'include',
# 'personal_email': 'include',
# 'personal_contact_number': 'include',
# 'twitter_profile_id': 'include',
# 'facebook_profile_id': 'include',
# 'github_profile_id': 'include',
# 'extra': 'include',
# }

# response = requests.get(api_endpoint, params=params, headers=header_dic)
# print(f"Response Status Code: {response.status_code}")
# print(f"Response Text: {response.text}")
