
from bs4 import BeautifulSoup as bs
import requests as r
from dataclasses import dataclass, field
#from concurrent.futures import ThreadPoolExecutor
#from threading import Thread
import os

w='wsl wget -nv'
DOWNLOAD_FOLDER='./'

url_example="https://ree.juegocontrola.com/assets/js/keyboard/"

#os.environ['WWGETPY_PATH']='assets/js/keyboard/'

@dataclass
class ElementBuilder:
    domain: str
    name: str
    parent_path: str
    complete_path: str = field(init=False)
    complete_url: str = field(init=False)
    
    def __post_init__(self) -> None:
        self.complete_path=f"{self.parent_path}/{self.name}"
        self.complete_url=f"{self.domain}/{self.complete_path}"
        
    def is_folder(self):
        name=self.name
        is_folder_v=True
        if len(name.split('.'))>=2:
            is_folder_v=False
        return is_folder_v
    
    def build_element(self):
        if self.is_folder():
            return Folder(self.domain,self.name,
                            self.parent_path,
                            self.complete_path,
                            self.complete_url)
        
        else:
            return File(self.domain,self.name,
                            self.parent_path,
                            self.complete_path,
                            self.complete_url)
    
    def run_element(self):
        if self.is_folder():
            print(f'***FOLDER \n {self.complete_path} folder is going to be created')
            Folder(self.domain,self.name,
                            self.parent_path,
                            self.complete_path,
                            self.complete_url).download()
        else:
            #print(f'---FILE \n {self.name} is going to be download')
            File(self.domain,self.name,
                            self.parent_path,
                            self.complete_path,
                            self.complete_url).download()


@dataclass
class Folder(ElementBuilder):
    complete_path: str # This address is needed to know the local destination
    complete_url: str # This address is needed to know the web source
    
    def run_source(self):
        print(f'A new Source was created for {self.name}')
        Source(path=self.complete_path).run_all_elements()
        
    def download(self):
        try:
            # Call download for each file            
            #File(self.domain,self.name,
            #                self.parent_path,
            #                self.complete_path,
            #               self.complete_url).download()
            
            # Run a source for this folder
            if self.is_folder():
                self.run_source()
                #Thread(target=self.run_source).start()
            else:
                print('It is a FILE but it was created as FOLDER!!!')
            exec_msg=f'It was possible to manage {self.name}.'
            print(exec_msg)
         
        except Exception as e:
            exec_msg=f'It WASNT possible to manage {self.name} because of {str(e)}.'
            print(exec_msg)
        


@dataclass
class File(ElementBuilder):
    complete_path: str # This address is needed to know the local destination
    complete_url: str # This address is needed to know the web source
    
    def download(self):
        #complete_path=self.complete_path#.replace("/","\\")
        try:
            os.system(f'{w} {self.complete_url} -P {DOWNLOAD_FOLDER}\{self.parent_path}')
            exec_msg=f'It was possible to get the file {self.name} in {self.parent_path}.'
            print(self.complete_path)
        except Exception as e:
            exec_msg=f'It WASNT possible to get the file {self.name} because of {str(e)}.'
        
        return exec_msg

@dataclass
class Source:
    domain: str = 'https://ree.juegocontrola.com'
    path: str = 'assets/'
    url: str = field(init=False)
    
    def __post_init__(self):
        self.url=f"{self.domain}/{self.path}"
    
    def get_all_elements(self):
        str_html=r.get(self.url).text
        raw_html=bs(str_html)
        all_elements_names=[a['href'] for a in raw_html.find_all('a')
                                        if "?" not in a['href']
                                        and "Parent Directory" not in a.text
                                        ]
        
        all_elements=[]
        for e in all_elements_names:
            all_elements.append(ElementBuilder(
                                domain=self.domain,
                                name=e,parent_path=self.path
                                ).build_element())
        return all_elements
    
    def run_all_elements(self) -> None:
        str_html=r.get(self.url).text
        raw_html=bs(str_html)
        all_elements_names=[a['href'] for a in raw_html.find_all('a') if "?" not in a['href']]
        print(f"These are all the elements:\n")
        for e in all_elements_names: print(f"    - {e}\n")
        
        for e in all_elements_names:
            ElementBuilder(domain=self.domain,
                           name=e,parent_path=self.path
                           ).run_element()

@dataclass
class Manager():
    domain=os.environ.get('WWGETPY_DOMAIN','https://ree.juegocontrola.com')
    path=os.environ.get('WWGETPY_PATH','assets/')

    s = Source(domain=domain,path=path)
    
    
    def download_all_files(self) -> None:
        all_elem=self.s.get_all_elements()
        for e in all_elem: e.download()
        

if __name__=='__main__':
    m=Manager().download_all_files()

