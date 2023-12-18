import requests

class TikTok_verify:

    def verifyVideo(2e__i, videoID):

        url = f"https://www.tiktok.com/@{2e__i}/video/{videoID}"

        payload = {}
        headers = {
            'authority': 'www.tiktok.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': 'msToken=v-s87FxGi8yQHIBk5QHg8SsfvJ3tpEzQyMVMyk7A7v1Yf89HkPQNXJs0VtHimsVfZdUofuvzagaAsNBcVXJT4M4A9xVMcToNc_5s6j_oH0prruGgIF7GQQOar6Z8Qyy2WgBBMKA=; tt_csrf_token=W6w7pL0I-yHeXdP79zvXK_5g_Teos54xk8U0; __tea_cache_tokens_1988={%22_type_%22:%22default%22}; csrf_session_id=8c8ece9e645172e2bb6935589702b6b3; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22version%22:%22v7%22}; _abck=15FD492EABF6D9746CF8471F7BEED63E~-1~YAAQ7wP9PgQucE+AAQAA+Hk+VgfSCBHH0r+eIa17oBt1OYyty5D/eyuc3PtJIWH8NGViDmbylyZf/ZyLSO7BCErrwav0ZTisiC66mieNTJIXSpBZuIpdvKOG4iM+r4bgP9yuO0JOINKDsIotQ/pQ/4+ej3G5ZanNJL0gPUWVn9Pcl56HQ3LgQrwtoZeHcU42U2mvALU7j5WCvRDC5rmH1BLSu2OBh7YGyVZJ+d11KEHNRo6vQFfhvUme4U9Y7QRdAk99lPP3xzzPQWnVOsl6L2CG+S5dtxjI0AlFoX38wbqh1BM1bQ2pVPVQ8wJBEq4ht+f7TfjNJq1hO4gZJvDdErTvJ2YinbL5nw6iJMBZh18Ted41Ig479Jz4xvuOjsrxhyeJuUzpAg2p6w==~-1~-1~-1; bm_sz=17C90B7AE2C1ACEBC93318FDD169D7ED~YAAQ7wP9PgYucE+AAQAA+Hk+Vg/geAZEghor7CxzqHUpimZEq8jvmLM02lfP2QzvTwud41Sxl41pZDWA58CYj0FKesS8b8KzQwYuex44/knN1AgAsEztY0A0Tr4AJ27gpqI2XZR8+PNoQIilf9l/DY7/ESbBb1P1ai7cBGVOkL+oeE5tm+eHzMtUMpIOxz0N7vWQRCHBZruHS//1sFukdcAs1jbx9dqHCeICREz0/Bewf0zf44IxLvKBDvrqmgPjAbIVIYISu+laRKSYVQ264QSMyuDReSLl39ToDEjkI2mci5E=~4604470~4343365; bm_mi=6EAA138635BEC2921BD64FBC2A684978~HwzUhvvngHabbgiGZrXKTREofnELl2LlYcwQkSNFFuPSl3KlML0LpeRl0FWTkpHPzfMtDsE632fxR1niB0Rmi6gNTggvQA6aR9mZO+AbLt7MRiDB8g6YmunOthiY8rNYBfzXdmw1B/slFxxgmgpIoLr/3sha4qgKhRu9UFtZuFBm65odo3CxcXkFZDSyEL3sIVRYjXL4bZ088EwcDLoTDhmz8wy0UgBraaTAneDdEZJZ9v1fLfxMzeeQcksD3Dsesv+W0mWk0lmNJxAp3LUlRA==; bm_sv=590E6C55D685A720E31047889A85D8E6~uQi9gXcpSkKGOugLNJg8WjS0veG7pVj5btdjzyowtIqf/gnYpYNAGYCy3b6LTQOLm8bRn9YxDmAj+Zvb9rd1XqnveSyR7HAcVNOYiovJJvcam6obLRUlDiDAfCTpawtioTdc8TYmCUdLueygK1Fudgckz0G0OX7MoRX+sxuHhm8=; ak_bmsc=1E962BD1E2797AD76D792126DD415DBF~000000000000000000000000000000~YAAQzwP9PrpDbE+AAQAAmRxDVg/fJZvnBXx8KMSLJ19NqNFGrmtrHMToFw3icgyKFR9uns5cyRkzUnVyG1ZOjuqP2ftBhDMQwaVw49QnOIdGzzpbWn0EmPxsgO6peg6quZiUch/eDc+b7eCbqCk0+TRk1e0HpGTphPZz33UtvN22f5BMjhuI5MxWR/0vEjcnu9s3o43+Dib432mBuhmudM9/JODu6O3xtVEgEjvgrEQrDhCOxAog9hnklZJQy0+tpgZdj/lShMR2qRfx7fnhPleDc70kxS4Z6b7MDod6Rj4/qU1LjJZmXFHReO2xn4vPyXJ5Me5uauZUXxOyguubYO5EznoMm45cdRZFNBr+xKTew2j6QDFn40KqZH9S35BHnPq3A+M/RQeWMLIIhMtB3QP9b2hIFb4bAx/xMJZgvsnC+K7BcUtFOdRGw/RCLR3xFXBhdOyBFxM3sXYNoI9Ka0pf; passport_csrf_token=b592df1ecadac9406b331b4c7c354175; passport_csrf_token_default=b592df1ecadac9406b331b4c7c354175; cmpl_token=AgQQAPOYF-RO0rJdC1BcMJ08-CbXHT5aP4QTYMBUUg; passport_auth_status=fe82aa0745a44f6e917782e3548b6e51%2C; passport_auth_status_ss=fe82aa0745a44f6e917782e3548b6e51%2C; sid_guard=1099b1229a8ef8294fc86ea75ee86597%7C1650718463%7C5184000%7CWed%2C+22-Jun-2022+12%3A54%3A23+GMT; uid_tt=362135ae7fd5d820b6b939fd9ba37f3f7f88200487152b7b8d4fb6b67edc11a6; uid_tt_ss=362135ae7fd5d820b6b939fd9ba37f3f7f88200487152b7b8d4fb6b67edc11a6; sid_tt=1099b1229a8ef8294fc86ea75ee86597; sessionid=1099b1229a8ef8294fc86ea75ee86597; sessionid_ss=1099b1229a8ef8294fc86ea75ee86597; sid_ucp_v1=1.0.0-KGJlMzBiNzQ1ODE4OWVkMzZlODU2ZjFmZGY3Y2VjYzYxMDVjMDJmNjMKHwiFiImg_b75sWIQ_-2PkwYYswsgDDD_7Y-TBjgIQBIQAxoGbWFsaXZhIiAxMDk5YjEyMjlhOGVmODI5NGZjODZlYTc1ZWU4NjU5Nw; ssid_ucp_v1=1.0.0-KGJlMzBiNzQ1ODE4OWVkMzZlODU2ZjFmZGY3Y2VjYzYxMDVjMDJmNjMKHwiFiImg_b75sWIQ_-2PkwYYswsgDDD_7Y-TBjgIQBIQAxoGbWFsaXZhIiAxMDk5YjEyMjlhOGVmODI5NGZjODZlYTc1ZWU4NjU5Nw; store-country-code=gb; tt-target-idc=useast1a; store-idc=maliva; ttwid=1%7CDaMCmHf81jAgLpKNXBp2GYpA6JMsnG9MxtR2x3MEVbA%7C1650721561%7C1287328e90f34d6083910d476c5920071dff88a4fe61937af2100f5e2d8c2780; odin_tt=4a78f37b69588996621181c011743ccaa84bb434f6e9cb9aa5b821d7a91357cdf28a2a7061607be883026874f97c89cf1cf1f3251ce20a4ddc6da4a4e267181eea43a079caf2f033421275f66adb2542; msToken=t1yujoW61u01PsVPXKWr5vQbl33Q3prL2NX6hPHrWgVoCnz5hOopcYPmcbFp_er5-6Ilb68F72e_0n4paXtaWC7FlHJap3JMp6qelqz0YBm-nYPNC8IarAPZ7ntb0M04b_OYETE=; passport_fe_beating_status=false; msToken=wDpho-rL03hmMcL_hlfzHD9nZhsXQMbgp5y3mouTnhXaZrpfeDYE3wFOtJv8W0MMNWrCanaKQWnOidjuPStp5LomTwLJLT-k5D4JWq435S2CV6fDFnbXZF6QyYiDNlArZIYcJEw=; odin_tt=d119969164d5b90c8c2221b7fa29d8ed907242edc3f5fa0a7b2da3f494ae16c691f5ef66b8b9189002da5ce5c9d17112bf573cbf3ca1da85471b353c71b07dc8',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }

        r = requests.request("GET", url, headers=headers, data=payload)

        if r.status_code == 200:
            return True
        else:
            return False

