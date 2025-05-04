import os

def cleanup(file_name):
    os.remove(file_name+'_misaal_temp_file.legalize.ll')
    os.remove(file_name+'_misaal_temp_file.linked.ll')
    os.remove(file_name+'_misaal_temp_file.linked.bc')
    os.remove(file_name+'_misaal_temp_file.ll')
    os.remove(file_name+'_s_exp')
    os.remove(file_name+'_misaal.py')