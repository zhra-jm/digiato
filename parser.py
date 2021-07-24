from bs4 import BeautifulSoup


class Parser:

    def __init__(self):
        self.soup = None

    @property
    def title(self):
        title_selector = '#global_wrap > div.digi-container.fixed-width.' \
                         'guttered.paged.margin-top-50> div.paper.white > ' \
                         'section > section > article > header > div > h1'
        title = self.soup.select_one(title_selector)
        if title:
            return title.text

    @property
    def author(self):
        author_selector = '#global_wrap > div.digi-container.fixed-width.' \
                          'guttered.paged.margin-top-50 > div.paper.white > section > ' \
                          'section > article > header > div > div > span:nth-child(2) > a'
        author = self.soup.select_one(author_selector)
        if author:
            return author.text

    @property
    def date_written(self):
        date_written_selector = '#global_wrap > div.digi-container.fixed-width.guttered.' \
                                'paged.margin-top-50 > div.paper.white > section > section >' \
                                ' article > header > div > div > span:nth-child(4) > a'
        date_written = self.soup.select_one(date_written_selector)
        if date_written:
            return date_written.text

    @property
    def pdf_link(self):
        pdf_link = self.soup.select_one('#download-pdf')
        if pdf_link:
            return pdf_link.attrs['href']

    @property
    def text(self):
        text_selector = '#global_wrap > div.digi-container.fixed-width.' \
                        'guttered.paged.margin-top-50 > div.paper.white > ' \
                        'section > section > article > div.digi-container.guttered' \
                        ' > div.article-content > p:nth-child(1)'
        text = self.soup.select_one(text_selector)
        if text:
            return text.text

    def parse(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(title=self.title, author=self.author, date_written=self.date_written,
                    pdf_link=self.pdf_link, text=self.text)
        return data

