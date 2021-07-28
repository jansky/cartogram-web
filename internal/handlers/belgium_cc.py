import settings
import handlers.base_handler
import csv

class CartogramHandler(handlers.base_handler.BaseCartogramHandler):

    def get_name(self):
        return "Belgium (ext ring counterclockwise)"

    def get_gen_file(self):
        return "{}/belgium_cc_processedmap.json".format(settings.CARTOGRAM_DATA_DIR)
    
    def validate_values(self, values):

        if len(values) != 3:
            return False
        
        for v in values:
            if type(v) != float:
                return False

        return True
    
    def gen_area_data(self, values):
        return """cartogram_id,Region Data,Region Name,Inset
1,{},Bruxelles,C
2,{},Vlaanderen,C
3,{},Wallonie,C""".format(*values)
    
    def expect_geojson_output(self):
        return True

    def csv_to_area_string_and_colors(self, csvfile):

        return self.order_by_example(csv.reader(csvfile), "Region", 0, 1, 2, 3, ["Bruxelles","Vlaanderen","Wallonie"], [0.0 for i in range(0,3)], {"Bruxelles":"1","Vlaanderen":"2","Wallonie":"3"})
