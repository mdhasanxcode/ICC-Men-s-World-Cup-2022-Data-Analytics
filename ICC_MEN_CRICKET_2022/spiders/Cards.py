import scrapy


class Cards(scrapy.Spider):
    name = 'Cards'
    allowed_domains = ['stats.espncricinfo.com']
    

    def start_requests(self):
        yield scrapy.Request(url="http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament")

    def parse(self, response):
        data = []
        

        for i in range(1,46):
            for j in range(1,8):
                    if j== 1:
                        products = {
                            'Team 1'        : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/text()').get(),
                            'Team 2'        : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/text()').get(),
                            'Winner'        : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/text()').get(),
                            'Margin'        : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/text()').get(),
                            'Ground'        : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/text()').get(),
                            'Match Date'    : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/text()').get(),
                            'Score Card No' : response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/text()').get(),
                            'Link' : "https://stats.espncricinfo.com/"+response.xpath(f'//tr[@class="data1"][{i}]/td[{j}]/a/@href').get()
                            }
            data.append(products)
        i+=1
        
        return data