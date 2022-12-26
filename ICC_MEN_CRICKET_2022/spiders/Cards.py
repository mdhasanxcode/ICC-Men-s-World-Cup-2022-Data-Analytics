import scrapy


class Cards4Spider(scrapy.Spider):
    name = 'Cards'
    allowed_domains = ['stats.espncricinfo.com']
    

    def start_requests(self):
        yield scrapy.Request(url="http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament")

    def parse(self, response):

        i = 1
        for card in response.xpath(f'//tr[@class="data1"]'):
            card = response.xpath(f'//tr[@class="data1"][{i}]')
            yield{
                'Team 1'        : card.xpath(f'.//td[1]/a/text()').get(),
                'Team 2'        : card.xpath(f'.//td[2]/a/text()').get(),
                'Winner'        : card.xpath(f'.//td[3]/a/text()').get(),
                'Margin'        : card.xpath(f'.//td[4]/text()').get(),
                'Ground'        : card.xpath(f'.//td[5]/a/text()').get(),
                'Match Date'    : card.xpath(f'.//td[6]/text()').get(),
                'Score Card No' : card.xpath(f'.//td[7]/a/text()').get(),
                'Link' : "https://stats.espncricinfo.com/"+card.xpath(f'.//td[7]/a/@href').get()
                }
            i+=1