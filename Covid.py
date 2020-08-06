from bs4 import BeautifulSoup
import requests


class Covid():
    def __init__(self):
        self.url = 'https://www.mygov.in/covid-19/'

    def get_data_country(self):
        try:
            response = requests.get('https://www.mygov.in/covid-19/')
            #soup
            soup = BeautifulSoup(response.text,'html.parser')
            total_case = soup.find('div',{"class": "t_case"})
            total_case = total_case.find('span')
            active_case = soup.find('div',{"class": "active-case"})
            active_case = active_case.find('span')
            recovered_case = soup.find('div',{"class": "discharge"})
            recovered_case = recovered_case.find('span')
            deaths = soup.find('div',{"class": "death_case"})
            deaths=deaths.find('span')
            india_data = dict()
            india_data["total_case"] = total_case.text
            india_data["active_case"]= active_case.text
            india_data["recovered"]= recovered_case.text
            india_data["deaths"]= deaths.text
            return india_data
        except:
            return 0

    def get_data_state(self):
        try:
            response = requests.get('https://www.mygov.in/covid-19/')
            #soup
            soup = BeautifulSoup(response.text,'html.parser')
            states = dict()
            states["0"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["1"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["2"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["3"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["4"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["5"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["6"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["7"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["8"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["9"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["10"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["11"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["12"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["13"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["14"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["15"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["16"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["17"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["18"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["19"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["20"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["21"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["22"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["23"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["24"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["25"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["26"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["27"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["28"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["29"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["30"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["31"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["32"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["33"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["34"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            states["35"]={"name":"","data":{'total':0,'active':0,'recovered':0,'deaths':0}}
            table = soup.find('table')
            rows = table.findAll('tr')
            for i in range(1,37):
                states[str(i-1)]["name"]=rows[i].findAll('td')[0].text
                states[str(i-1)]["data"]["total"]=rows[i].findAll('td')[1].text
                states[str(i-1)]["data"]["active"]=rows[i].findAll('td')[2].text
                states[str(i-1)]["data"]["recovered"]=rows[i].findAll('td')[3].text
                states[str(i-1)]["data"]["deaths"]=rows[i].findAll('td')[4].text
            return states    
        except:
            return 0

    def get_heading(self):
        try:
            response = requests.get('https://www.mygov.in/covid-19/')
            #soup
            soup = BeautifulSoup(response.text,'html.parser')

            heading = dict()
            title = soup.find('div',{"class":"info_title"})
            titled = title.find('p')
            heading["title"]=titled.text
            stamp = title.find('span').text
            heading["stamp"]=stamp
            return heading
        except:
            return 0











            

























    

            
