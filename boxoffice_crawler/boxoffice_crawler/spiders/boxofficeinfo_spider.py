<<<<<<< HEAD
import scrapy

from boxoffice_crawler.items import BoxofficeCrawlerItem
from datetime import datetime

class BoxofficeSpider(scrapy.Spider):
    name = "BoxOfficeMojo"
    allowed_domains = ["boxofficemojo.com"]
    start_urls = []

<<<<<<< HEAD
    for year in range(2000, 2023):
=======
    for year in range(1990, 2023):
>>>>>>> 8036ffbd0bc95fc8bf1cd15f679204a4e88c9006
        start_urls.append(f"https://www.boxofficemojo.com/year/{year}/")

    def parse(self, response):
        for tr in response.xpath('//*[@id="table"]/div/table/tr')[1:]:
            href = tr.xpath('./td[2]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        item = BoxofficeCrawlerItem()
        item["title"] = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        item["domestic_revenue"] = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[1]/span[2]/span/text()')[0].extract()
        item["world_revenue"] = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[3]/span[2]/a/span/text()')[0].extract()

        elements = []
        for div in response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div')[0:]:
            elements.append(' '.join(div.xpath('./span[1]/text()')[0].extract().split()))

        #Distributor
        if 'Distributor' in elements:
            d = elements.index('Distributor') + 1
            loc_dist = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(d)
            item["distributor"] = response.xpath(loc_dist)[0].extract()
        else:
            item["distributor"] = "N/A"

        # Opening Revenue
        if 'Opening' in elements:
           o = elements.index('Opening') + 1
           loc_open_rev = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/span/text()'.format(o)
           try:
               item["opening_revenue"] = response.xpath(loc_open_rev)[0].extract()
           except:
               item["opening_revenue"] = "N/A"
        else:
            item["opening_revenue"] = "N/A"

        # Opening Theaters
        if 'Opening' in elements:
           o = elements.index('Opening') + 1
           loc_open_theater = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(o)
           try:
               item["opening_theaters"] = response.xpath(loc_open_theater)[0].extract().split()[0]
           except:
               item["opening_theaters"] = "N/A"
        else:
            item["opening_theaters"] = "N/A"

        # Budget
        if 'Budget' in elements:
            b = elements.index('Budget') + 1
            loc_budget = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/span/text()'.format(b)
            item["budget"] = response.xpath(loc_budget)[0].extract()
        else:
            item["budget"] = "N/A"

        # MPAA
        if 'MPAA' in elements:
            m = elements.index('MPAA') + 1
            loc_MPAA = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(m)
            item["MPAA"] = response.xpath(loc_MPAA)[0].extract()
        else:
            item["MPAA"] = "N/A"

        # Genres
        if 'Genres' in elements:
            g = elements.index('Genres') + 1
            loc_genres = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(g)
            item["genres"] = ",".join(response.xpath(loc_genres)[0].extract().split())
        else:
            item["genres"] = "N/A"

        # In Release
        if 'In Release' in elements:
            r = elements.index('In Release') + 1
            loc_release = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(r)
            item["in_release"] = response.xpath(loc_release)[0].extract().split()[0]
        else:
            item["in_release"] = "N/A"
        # Realease Day
        if 'Release Date' in elements:
            r = elements.index('Release Date') + 1
            loc_release = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/a/text()'.format(r)
            release_date_str = response.xpath(loc_release).get(default="N/A")
           

            # Parse the date string and format it in "day/month/year"
            try:
                release_date = datetime.strptime(release_date_str, "%b %d, %Y")
                item["release_date"] = release_date.strftime("%d/%m/%Y")
            except ValueError:
                item["release_date"] = "N/A"
        else:
            item["release_date"] = "N/A"
            
        yield item
=======
import scrapy

from boxoffice_crawler.items import BoxofficeCrawlerItem
from datetime import datetime

class BoxofficeSpider(scrapy.Spider):
    name = "BoxOfficeMojo"
    allowed_domains = ["boxofficemojo.com"]
    start_urls = []

    for year in range(1990, 2023):
        start_urls.append(f"https://www.boxofficemojo.com/year/{year}/")

    def parse(self, response):
        for tr in response.xpath('//*[@id="table"]/div/table/tr')[1:]:
            href = tr.xpath('./td[2]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    

    def parse_page_contents(self, response):
        item = BoxofficeCrawlerItem()
        item["title"] = response.xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1/text()')[0].extract()
        item["domestic_revenue"] = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[1]/span[2]/span/text()')[0].extract()
        item["world_revenue"] = response.xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div/div[3]/span[2]/a/span/text()')[0].extract()

        elements = []
        for div in response.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div')[0:]:
            elements.append(' '.join(div.xpath('./span[1]/text()')[0].extract().split()))

        #Distributor
        if 'Distributor' in elements:
            d = elements.index('Distributor') + 1
            loc_dist = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(d)
            item["distributor"] = response.xpath(loc_dist)[0].extract()
        else:
            item["distributor"] = "N/A"

        # Opening Revenue
        if 'Opening' in elements:
           o = elements.index('Opening') + 1
           loc_open_rev = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/span/text()'.format(o)
           try:
               item["opening_revenue"] = response.xpath(loc_open_rev)[0].extract()
           except:
               item["opening_revenue"] = "N/A"
        else:
            item["opening_revenue"] = "N/A"

        # Opening Theaters
        if 'Opening' in elements:
           o = elements.index('Opening') + 1
           loc_open_theater = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(o)
           try:
               item["opening_theaters"] = response.xpath(loc_open_theater)[0].extract().split()[0]
           except:
               item["opening_theaters"] = "N/A"
        else:
            item["opening_theaters"] = "N/A"

        # Budget
        if 'Budget' in elements:
            b = elements.index('Budget') + 1
            loc_budget = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/span/text()'.format(b)
            item["budget"] = response.xpath(loc_budget)[0].extract()
        else:
            item["budget"] = "N/A"

        # MPAA
        if 'MPAA' in elements:
            m = elements.index('MPAA') + 1
            loc_MPAA = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(m)
            item["MPAA"] = response.xpath(loc_MPAA)[0].extract()
        else:
            item["MPAA"] = "N/A"
        if 'Running Time' in elements:
            r = elements.index('Running Time') + 1
            loc_running = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(r)
            running_time_str = response.xpath(loc_running).get(default="N/A")

            # Parse the running time string
            try:
                running_time = parse_running_time(running_time_str)
                item["running_time"] = running_time
            except ValueError:
                item["running_time"] = "N/A"
        else:
            item["running_time"] = "N/A"

        # Genres
        if 'Genres' in elements:
            g = elements.index('Genres') + 1
            loc_genres = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(g)
            item["genres"] = ",".join(response.xpath(loc_genres)[0].extract().split())
        else:
            item["genres"] = "N/A"

        # In Release
        if 'In Release' in elements:
            r = elements.index('In Release') + 1
            loc_release = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/text()'.format(r)
            item["in_release"] = response.xpath(loc_release)[0].extract().split()[0]
        else:
            item["in_release"] = "N/A"
        # Realease Day
        if 'Release Date' in elements:
            r = elements.index('Release Date') + 1
            loc_release = '//*[@id="a-page"]/main/div/div[3]/div[4]/div[{}]/span[2]/a/text()'.format(r)
            release_date_str = response.xpath(loc_release).get(default="N/A")
           

            # Parse the date string and format it in "day/month/year"
            try:
                release_date = datetime.strptime(release_date_str, "%b %d, %Y")
                item["release_date"] = release_date.strftime("%d/%m/%Y")
            except ValueError:
                item["release_date"] = "N/A"
        else:
            item["release_date"] = "N/A"
         # Running Time
        
                
            
        yield item
def parse_running_time(running_time_str):
    # Split the string into parts
        parts = running_time_str.split()
        # Initialize the total running time
        running_time = 0
        # Iterate over the parts
        for i in range(0, len(parts), 2):
            # Get the number part
            number = int(parts[i])
            # Get the unit part
            unit = parts[i + 1]
            # If the unit is "hr", multiply the number by 60
            if "hr" in unit:
                number *= 60
            # Add the number to the total running time
            running_time += number
        return running_time
>>>>>>> d9aefeb7390689c0e1f1a12d905964a735950e9a
