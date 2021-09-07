from flask import Flask
from random_objects.rand_obj_creation import ObjectCreation
app = Flask(__name__)

random_obj = ObjectCreation()

app.add_url_rule('/generate_random_objects', view_func=random_obj.create_obj, methods=['POST']) # end point for random object generation
app.add_url_rule('/download_file', view_func=random_obj.get_csv_file, methods=['GET']) # end point to download file
app.add_url_rule('/get_file_size', view_func=random_obj.get_file_stats, methods=['GET']) # end point to check the file status
app.add_url_rule('/get_count', view_func=random_obj.get_count, methods=['GET']) # end point to get the count of objects

if __name__ == '__main__':
    app.run()
