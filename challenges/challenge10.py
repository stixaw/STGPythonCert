import unittest
import requests
import json

class Challenge10(unittest.TestCase):

    def test_get(self):
        r = requests.get('https://api.github.com/events')
        print(r)

    def test_search_copart_for_honda(self):
        cookie = 's_fid=3BFC35D460630745-31354C77F43D45F6; __cfduid=d522c6367c9915be293cba6b34b4ab9991565581886; s_vi=[CS]v1|2EA8711F0503200B-600011826001015B[CE]; OAID=066c33f79f0545bf809b8bc28ee2bf58; g2app.locationInfo=%7B%22countryCode%22%3A%22US%22%2C%22threeCharCountryCode%22%3A%22USA%22%2C%22stateName%22%3A%22Utah%22%2C%22stateCode%22%3A%22UT%22%2C%22cityName%22%3A%22Sandy%22%2C%22latitude%22%3A40.5794%2C%22longitude%22%3A-111.8816%2C%22zipCode%22%3A%2284070%22%2C%22countyName%22%3A%22Salt%20Lake%22%2C%22countyCode%22%3A%22035%22%2C%22metroName%22%3A%22%22%2C%22metroCode%22%3A%22%22%2C%22accuracy%22%3A%224%22%7D; g2app.searchResultsPageLength=100; incap_ses_731_242093=TaWVN64LJg6XmybSsSUlCpoerl0AAAAAjzzv88hL1kmr9x1Y8y8Tmg==; g2usersessionid=023c5fb0412f4eeeabb81f3a16fe981a; G2JSESSIONID=832D16AC5627AD221C558FE81AC75957-n1; userLang=en; visid_incap_242093=xkACFTEiTNWaPqasMe1J2DfiUF0AAAAAQ0IPAAAAAACAtbOPAUIHcUNsuF64OkbSe+3oAnxQWqAS; copartTimezonePref=%7B%22displayStr%22%3A%22MDT%22%2C%22offset%22%3A-6%2C%22dst%22%3Atrue%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; timezone=America%2FDenver; _ga=GA1.2.1879390003.1571692199; _gid=GA1.2.544916175.1571692199; _gat=1; s_depth=1; s_pv=public%3Ahomepage; s_vnum=1574284199552%26vn%3D1; s_invisit=true; s_lv_s=More%20than%2030%20days; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=79423db72fe159b4ef3a425b9e423f26; __gads=ID=898431106960e754:T=1571692199:S=ALNI_MZJvucp01R-MFpZ5wcbeHGk9RSWIA; _fbp=fb.1.1571692202395.1105687356; s_ppvl=18; s_nr=1571692223767-New; s_lv=1571692223769; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dpublic%25253Ahomepage%2526link%253DSearch%2526region%253Dsearch-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dpublic%25253Ahomepage%2526pidt%253D1%2526oid%253DSearch%2526oidt%253D3%2526ot%253DSUBMIT; s_ppv=public%253Ahomepage%2C50%2C11%2C714%2C984%2C713%2C1440%2C900%2C2%2CP'

        my_headers = {
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": "18bc1362-0eb5-4778-a784-f68ca0bfece3",
            "origin": "https://www.copart.com",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": 'application/json, text/javascript, */*; q=0.01',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": cookie
        }

        form_data = {
            "columns[0][data]": "0",
            "columns[0][name]": "",
            "columns[0][orderable]": "false",
            "columns[0][search][regex]": "false",
            "columns[0][search][value]": "",
            "columns[0][searchable]": "true",
            "columns[10][data]": "10",
            "columns[10][name]": "",
            "columns[10][orderable]": "true",
            "columns[10][search][regex]": "false",
            "columns[10][search][value]": "",
            "columns[10][searchable]": "true",
            "columns[11][data]": "11",
            "columns[11][name]": "",
            "columns[11][orderable]": "true",
            "columns[11][search][regex]": "false",
            "columns[11][search][value]": "",
            "columns[11][searchable]": "true",
            "columns[12][data]": "12",
            "columns[12][name]": "",
            "columns[12][orderable]": "true",
            "columns[12][search][regex]": "false",
            "columns[12][search][value]": "",
            "columns[12][searchable]": "true",
            "columns[13][data]": "13",
            "columns[13][name]": "",
            "columns[13][orderable]": "true",
            "columns[13][search][regex]": "false",
            "columns[13][search][value]": "",
            "columns[13][searchable]": "true",
            "columns[14][data]": "14",
            "columns[14][name]": "",
            "columns[14][orderable]": "false",
            "columns[14][search][regex]": "false",
            "columns[14][search][value]": "",
            "columns[14][searchable]": "true",
            "columns[15][data]": "15",
            "columns[15][name]": "",
            "columns[15][orderable]": "false",
            "columns[15][search][regex]": "false",
            "columns[15][search][value]": "",
            "columns[15][searchable]": "true",
            "columns[1][data]": "1",
            "columns[1][name]": "",
            "columns[1][orderable]": "false",
            "columns[1][search][regex]": "false",
            "columns[1][search][value]": "",
            "columns[1][searchable]": "true",
            "columns[2][data]": "2",
            "columns[2][name]": "",
            "columns[2][orderable]": "true",
            "columns[2][search][regex]": "false",
            "columns[2][search][value]": "",
            "columns[2][searchable]": "true",
            "columns[3][data]": "3",
            "columns[3][name]": "",
            "columns[3][orderable]": "true",
            "columns[3][search][regex]": "false",
            "columns[3][search][value]": "",
            "columns[3][searchable]": "true",
            "columns[4][data]": "4",
            "columns[4][name]": "",
            "columns[4][orderable]": "true",
            "columns[4][search][regex]": "false",
            "columns[4][search][value]": "",
            "columns[4][searchable]": "true",
            "columns[5][data]": "5",
            "columns[5][name]": "",
            "columns[5][orderable]": "true",
            "columns[5][search][regex]": "false",
            "columns[5][search][value]": "",
            "columns[5][searchable]": "true",
            "columns[6][data]": "6",
            "columns[6][name]": "",
            "columns[6][orderable]": "true",
            "columns[6][search][regex]": "false",
            "columns[6][search][value]": "",
            "columns[6][searchable]": "true",
            "columns[7][data]": "7",
            "columns[7][name]": "",
            "columns[7][orderable]": "true",
            "columns[7][search][regex]": "false",
            "columns[7][search][value]": "",
            "columns[7][searchable]": "true",
            "columns[8][data]": "8",
            "columns[8][name]": "",
            "columns[8][orderable]": "true",
            "columns[8][search][regex]": "false",
            "columns[8][search][value]": "",
            "columns[8][searchable]": "true",
            "columns[9][data]": "9",
            "columns[9][name]": "",
            "columns[9][orderable]": "true",
            "columns[9][search][regex]": "false",
            "columns[9][search][value]": "",
            "columns[9][searchable]": "true",
            "draw": "1",
            "freeFormSearch": "true",
            "length": "20",
            "page": "0",
            "query": "honda",
            "search[regex]": "false",
            "search[value]": "",
            "size": "20",
            "start": "0",
            "watchListOnly": "false"
        }

        # search_list = ["honda", "toyota", "GMC", "ford", "BMW", "nissan", "dodge", "hyundai", "chrysler", "subaru"]
        search_list = []
        url = 'https://www.copart.com/public/lots/search'

        f = open('data.txt', 'w')

        for model in search_list:
            form_data['query'] = model

            r = requests.post(url, headers=my_headers, data=form_data)
            response = r.json()

            # get car model in search
            data = response['data']
            query = data['query']
            query_2 = query['query']
            car_model = query_2[0]

            # get totalElements from results
            results = data['results']
            total_elements = results['totalElements']

            message = '{0} - {1}'.format(car_model, total_elements)
            print(message)
            f.write(message + '\n')
        f.close()


if __name__ == '__main__':
    unittest.main()
