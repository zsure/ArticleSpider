# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    #start_urls = ['http://blog.jobbole.com/110287/']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    def parse(self, response):
      """
      parse需要实现的功能：
      1、获取文章列表页中的文章url并交给scrapy下载后并进行解析
      2、获取下一页的url并交给scrapy进行下载，下载完成后交给parse
      """
      #解析列表页中的所有文章url并交给scrapy下载
      post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
      for post_url in post_urls:
          print(post_url)
      Request(url=parse.urljoin(),callback= self.parse_detail)

    def parse_detail(self, response):
        #xpath mode
        # title = response.xpath('// div[@class = "entry-header"] / h1/text()')
        # title = response.xpath('// *[ @ id = "post-110287"] / div[1] / h1/text()').extract()[0]
        # create_date = response.xpath('//*[@id="post-110287"]/div[2]/p/text()[1]').extract()[0].strip().replace("·","").strip()
        # parise_numbers = response.xpath('//*[@id="110287votetotal"]/text()').extract()[0]
        # fav_numbers = response.xpath('//*[@id="post-110287"]/div[3]/div[9]/span[2]/text()').extract()[0]
        # match_re = re.match(r".*?(\d+).*",fav_numbers)
        # if match_re:
        #     fav_numbers = match_re.group(1)
        # comment_numbers = response.xpath('//*[@id="post-110287"]/div[3]/div[9]/a/span/text()').extract()[0].strip()
        # match_re = re.match(r".*?(\d+).*",comment_numbers)
        # if match_re:
        #     comment_numbers = match_re.group(1)
        # content = response.xpath("//div[@class='entry']").extract()[0]
        # tag = response.xpath('//*[@id="post-110287"]/div[3]/div[2]/a/text()').extract()[0]
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)

        #css mode
        title = response.css(".entry-header h1::text").extract_first()
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract_first().strip().replace("·","").strip()
        praise_numbers =  response.css(".vote-post-up  h10::text").extract_first()
        fav_numbers = response.css("span.bookmark-btn::text").extract_first()
        match_re = re.match(r".*?(\d+).*", fav_numbers)
        if match_re:
             fav_numbers = match_re.group(1)
        comment_numbers = response.css("a[href='#article-comment'] span::text").extract_first()
        match_re = re.match(r".*?(\d+).*", comment_numbers)
        if match_re:
             comment_numbers = match_re.group(1)
        content = response.css("div.entry").extract_first()
        tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        pass
