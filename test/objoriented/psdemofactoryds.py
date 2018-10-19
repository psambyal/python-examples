'''
Created on 07-Jun-2018

@author: pritika sambyal
'''
from glob import glob
import abc 
# abstract base class in python
from zipfile import ZipFile
from tarfile import TarFile

class Archive(metaclass=abc.ABCMeta) : # metaclass determine behaviour of other classes
    '''abstract class &mthod'''
    @abc.abstractmethod  #decorator to show abstract method
    def save(self):
        pass
    

class ZipArchive(Archive):
    def __init__(self, name, *args):
        self.name = name;
        self.archive_content = args
    
    def save(self):
        with ZipFile(self.name, mode='w') as zw:
            for file_name in self.archive_content:
                zw.write(file_name)


class TarArchive(Archive):
    pass
    
    
def make_archive(archive_name,*args, archive_type='zip'):
    '''factory method'''
    if archive_type =='zip':
        archive_instance =ZipArchive(archive_name,*args)
    elif archive_type =='tar':
        archive_instance = TarArchive()
        
    return archive_instance


if __name__ == '__main__':
    #print(glob('*.py'))
    archive = make_archive('pys.zip',*glob('*.py'))
    archive.save()
