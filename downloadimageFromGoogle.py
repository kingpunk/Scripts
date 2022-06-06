# First Section: Importing Libraries
import os
import requests
import PIL.Image as Image
import io
from bs4 import BeautifulSoup

imageSize= (500,500)
# Second Section: Declare important variables
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# Third Section: Build the main function
saved_folder = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\InternetDataset'


def main():
    
    
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    download_images()


# Fourth Section: Build the download function
def download_images():
    data = input("What is the image about? ")
    n_images = int(input('How many images do you want? '))

    download_path = os.path.join(saved_folder,data)

    if not os.path.exists(download_path):
        os.mkdir(download_path)

    print('searching...')

    search_url = "https://www.bing.com/images/search?q="+data+"&qs=n&form=QBIR&sp=-1&pq="+data+"&sc=8-3&cvid=FEA5B81ED5014D6E8FCA9C56747826E3&ghsh=0&ghacc=0&first=1&tsc=ImageHoverTitle"

    response = requests.get(search_url, headers=user_agent)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')


    results = soup.findAll('img', {'class': 'mimg'} )
    count = 1
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue


    print(f"Downloading {len(links)} images...")
    for i, link in enumerate(links):

        try:
            response = requests.get(link)
        except KeyError:
            continue
        img = Image.open(io.BytesIO(response.content))
        img = img.resize(imageSize)
        image_name = download_path + '/' + data + str(i+1) + '.jpg'
        img.save(image_name)
        #with open(image_name, 'wb') as fh:
            #fh.write(response.content)


# Fifth Section: Run your code
if __name__ == "__main__":
    # Third Section: Build the main function
    saved_folder = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\InternetDataset'
    main()