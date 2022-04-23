import requests
from Logger import Logger


class TikTok_Report:


    def Title(Content):
        global DebugMode
        if os.name in ('posix', 'ce', 'dos'):
            pass
        elif os.name == 'nt':
            os.system(f"title {Content}")
            return False
        else:
            pass

    def sendRequest(accountName, videoID, i):

        try:

            url = f"https://www.tiktok.com/aweme/v1/aweme/feedback/?app_language=en&app_name=tiktok_web&battery_info=0.12&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&channel=tiktok_web&cookie_enabled=true&current_region=GB&device_platform=web_pc&focus_state=true&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&lang=en&nickname={accountName}&object_id={videoID}&os=mac&priority_region=&reason=1024&referer=&region=GB&report_type=video&screen_height=900&screen_width=1440&target={videoID}&tz_name=Europe%2FLondon&video_id={videoID}&video_owner=%5Bobject%20Object%5D&webcast_language=en"

            payload = {}
            headers = {
                'authority': 'www.tiktok.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://www.tiktok.com/@ace_pings/video/7088763620779101446?is_copy_url=1&is_from_webapp=v1',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            response = response.json()

            if response["status_msg"] == "Thanks for your feedback":

                Logger.success(f"[TASK {i}] Sent Report: {response['extra']['logid']}")

            else:
                Logger.error((f"[TASK {i}] Could not send report"))

        except Exception as e:
            Logger.error(e)

