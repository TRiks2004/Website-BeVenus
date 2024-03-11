from pydantic_settings import BaseSettings
# from .__settings import env

from os import path

from enum import Enum

class ViewName(Enum):
    index = 'index'

class SettingsApp(BaseSettings):
    
    @property
    def path_folder_resources(self) -> str:
        dirname = path.dirname(__file__)
        parent_directory = path.dirname(dirname)
        
        folder_resources = 'resources'
        
        return path.join(parent_directory, folder_resources)
    
    @property
    def path_folder_static(self) -> str:
        subfolder_static = 'static'
        return path.join(self.path_folder_resources, subfolder_static)
    
    @property
    def path_folder_view(self) -> str:
        return path.join(self.path_folder_resources, 'views')
    
    def path_file_view(self, filename: ViewName) -> str:
        return path.join(self.path_folder_view, filename.value + '.html')

settings_app = SettingsApp()

class PathView():
    index = settings_app.path_file_view(ViewName.index)
    
    
    


