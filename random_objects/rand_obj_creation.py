import os
import traceback
from threading import Thread
from flask import jsonify, send_file, request
from constants import SUCCESS_CODE, EXCEPTION_MSG, ERROR_CODE, CSV_FILE, MSG, FILE_SIZE
from .utils import generate_random_alphanumeric, generate_random_string, generate_random_integers, generate_csv, \
    get_default_param, calaculate_count


class ObjectCreation:
    """
    this view is used to generate random objects of 4 different types
    random objects will be generated in background process and will be written in csv file
    """
    def create_obj(self):
        try:
            thread = Thread(target=generate_csv)
            thread.daemon = True
            thread.start()
            return jsonify({"msg": MSG, "data": CSV_FILE}), SUCCESS_CODE
        except Exception as e:
            traceback.print_exc()
            return jsonify({"msg": EXCEPTION_MSG, "data": []}), ERROR_CODE

    """
    this view is used to download file
     param = file_name
    """

    def get_csv_file(self):
        try:
            file_name = get_default_param(request, 'file_name', None)
            return send_file(file_name,
                         mimetype='text/csv',
                         attachment_filename=file_name,
                         as_attachment=True)
        except Exception as e:
            traceback.print_exc()
            return jsonify({"msg": EXCEPTION_MSG, "data": []}), ERROR_CODE

    """
    this view is used to check the status of file when available
    true: when file size is 2mb
    else false
    param = file_name
    """
    def get_file_stats(self):
        try:
            file_name = get_default_param(request, 'file_name', None)
            file_ready = False
            if os.path.isfile(file_name):
                size = round(os.stat(CSV_FILE).st_size / 1048576, 2)
                if size >= FILE_SIZE:
                    file_ready = True
            return jsonify({"msg":"", "data": file_ready}), SUCCESS_CODE
        except Exception as e:
            traceback.print_exc()
            return jsonify({"msg": EXCEPTION_MSG, "data": []}), ERROR_CODE

    """
    this view is used to get count for different random objects
    param=file_name
    """
    def get_count(self):
        try:
            file_name = get_default_param(request, 'file_name', None)
            data = calaculate_count(file_name)
            return jsonify({"msg": "", "data": data}), SUCCESS_CODE
        except Exception as e:
            traceback.print_exc()
            return jsonify({"msg": EXCEPTION_MSG, "data": []}), ERROR_CODE

