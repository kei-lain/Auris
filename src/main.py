#Project: Auris
#Author: Lainey "Lain" Tubbs
#About: Auris is a WIP AUR script that queries AUR packages


import  sys , os, platform , argparse,subprocess
import aur 
from bs4 import BeautifulSoup
from urllib.request import urlopen


 
item = ''
packageList = []
urls = []
count = 0
choice = 0
selection  = 0 
baseURL = ''
currentUser = ''
# distroderiv = ''
# distro = ''



Package = aur.Package('category_id','description','url_path','last_modified','name','out_of_date','id', 'first_submitted', 'maintainer','version','license','url', 'package_base','package_base_id','category_id')
parser = argparse.ArgumentParser(description='This is an aur helper written in Python: Auris!!')
parser.add_argument('-p', help='This is the argument to query a package to install!')
parser.add_argument('-d', help='Alter the default installation directory')
#parser.add_argument('-')
args = parser.parse_args()



# class initialSetup():
#     def __init__(self):
#         # self.distroderiv = distroderiv
#         # self.distro = distro



#     def initText(self,):
#         # distro = os.name()
#         # distroderiv = platform.linux_distribution
#         print(os.name)
#         print(platform.linux_distribution)
#         while os.path.isdir('/var/lib/pacman') == False:
#           os.mkdir('/var/lib/pacman')
#         while os.path.isdir('/var/cache/pacman/pkg/') == False:
#             os.mkdir('/var/cache/pacman/pkg/')
#         while os.path.isdir('/etc/pacman.d/gnupg') == False:
#             os.mkdir('/etc/pacman.d/gnupg')

if __name__ == "__main__":
    #print(args)
    # initial = initialSetup()
    # initial.initText()
    #print(os.name())
    print(platform.platform())
    
    while os.path.isdir('/var/lib/pacman') == False:
        os.mkdir('/var/lib/pacman')
    while os.path.isdir('/var/cache/pacman/pkg/') == False:
        os.mkdir('/var/cache/pacman/pkg/')
    while os.path.isdir('/etc/pacman.d/gnupg') == False:
        os.mkdir('/etc/pacman.d/gnupg')
    if os.getuid() == 0:
        sys.ext("Do not run this script as root")
    else:
       pass
    print(args.p)
    while args.p == None:
        sys.exit('No package to query')
    #Packages = aur.Package(category_id,description,first_submitted,id, last_modified, license, maintainer, name, num_votes, out_of date )
    item = aur.search(f'{args.p}')
    #print(item)
    for package in item:
        count += 1
        #packageList.append(package)
        print(f"{count}.{package}")
        #package.url()
        print("Description: ", package.description)
        print("Number of votes", package.num_votes)
        print("Package out of date: ", package.out_of_date)
        print("Project URL: ", package.url)
        print("Git Clone URL: ", package.package_base)
        packageList.append(package.package_base)
        urls.append(package.url)

        print('')
        print('')
        print('')
    #print(urls)
    selection = int(input(f"Go ahead and select which package you would like to install [1 - {count}"))
    choice = selection - 1
    print(urls[choice])
    baseURL = 'https://aur.archlinux.org/packages/'
    print(f"{baseURL}/{packageList[choice]}")
    page = urlopen(f'{baseURL}{packageList[choice]}')
    soup = BeautifulSoup (page, 'html.parser')
    tag = soup.select("a.copy")[0]
    result = tag.text
    #print(soup.find_all("git"))
    currentUser = os.getlogin()
    print(result)
    if os.path.isdir(f'/home/{currentUser}/Packages'):
        os.chdir(f'/home/{currentUser}/Packages')
    elif os.path.isdir(f'/home/{currentUser}/Packages') == False:
        os.mkdir(f'/home/{currentUser}/Packages')
        os.chdir(f'/home/{currentUser}/Packages')
    elif args.d != null:
        os.chdir(f'{args.d}')
    else: 
        pass

    os.system(f"git clone {result}")
    os.chdir(f'{packageList[choice]}')
    try:
        os.system('makepkg -si')
    except:
        os.system('makepkg -di')
        pass 


    # for a in soup.find_all(a.copy):
    #     print("Found the URL: ", a.copy)


    
