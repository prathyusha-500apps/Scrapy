import scrapy
class FlexjobsSpider(scrapy.Spider):
    name = "flexjobs"
    allowed_domains = ["www.flexjobs.com"]
    start_urls = ['https://www.flexjobs.com/search?search=python&location=']

    def parse(self, response):
        job_data=response.xpath("//ul[@class='p-0 ']//a").xpath('@href').getall()
        print(response.text)
        print(job_data)
        count = 0 
        for i in job_data:
            job_data[count] = f"https://www.flexjobs.com/{i}"
            count=count+1
            print(job_data)
        for job_link in job_data:
            yield scrapy.Request(url=job_link, callback=self.parse_job)

        # Extract the URL or element for the "next" button
        next_page = response.xpath("//a[@rel='next']/@href").get()
        if next_page:
            # Create a new request for the next page
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_job(self, response):
        print(response.text)
        job_listing = {}
        title = response.xpath("//h1/text()").get()
        Description=response.xpath("//div[@class='job-description']/text()").get()
        Dateposted = response.css('tr:nth-child(1) td::text').get().replace("\n","").replace("\t","").replace(" ","")
        RemoteWorkLevel = response.css('tr:nth-child(2) td::text').get().replace("\n","").replace("\t","").replace(" ","")  
        Jobtype = response.css('tr:nth-child(4) td::text').get().replace("\n","").replace("\t","").replace(" ","")
        Location = response.css('tr:nth-child(3) td::text').get().replace("\n","").replace("\t","").replace(" ","")
        CareerLevel = response.css('tr:nth-child(6) td::text').get().replace("\n","").replace("\t","").replace(" ","")
        JobSchedule = response.css('tr:nth-child(5) td::text').get().replace("\n","").replace("\t","").replace(" ","")
        job_listing['title'] = title
        job_listing['Description'] = Description
        job_listing['date posted'] = Dateposted
        job_listing['RemoteWorkLevel'] = RemoteWorkLevel
        job_listing['Jobtype'] = Jobtype
        job_listing['Location'] = Location
        job_listing['CareerLevel'] = CareerLevel
        job_listing['JobSchedule'] = JobSchedule
        yield job_listing
