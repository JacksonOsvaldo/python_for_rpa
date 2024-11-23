import os
import shutil

class OsManager:
    
    @classmethod
    def create_temp_folder(sefl, name_folder: str = 'temp'):
        if os.path.exists(name_folder):
            shutil.rmtree('temp')
            os.makedirs(name_folder)
        else:
            os.makedirs(name_folder)