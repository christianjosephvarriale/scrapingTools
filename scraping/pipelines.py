from scrapy.exporters import JsonLinesItemExporter
import re

class ExtractionPipeline(object):
    ''' exports to different JSON lines files based on url '''
    def open_spider(self, spider):
        self.f_lst = {}

    def close_spider(self, spider):
        for exporter in self.f_lst.values():
            exporter.finish_exporting()
            exporter.file.close()

    def _exporter_for_item(self, item, spider):
        url = item['url']
        ticker = re.search(r'/[A-Z]+/', url).group()[1:-1]
        metric = re.search(r'[A-Z]/.+p', url).group()[2:-2]
        f_name = f'{ticker}-{metric}'
        if f_name not in self.f_lst:
            f = open(f_name+'.jl', 'wb') 
            exporter = JsonLinesItemExporter(f)
            exporter.start_exporting()
            self.f_lst[f_name] = exporter
        return self.f_lst[f_name]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item, spider)
        item.pop('url') # not needed
        exporter.export_item(item)
        return item
