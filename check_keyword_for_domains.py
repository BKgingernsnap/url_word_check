import requests
import sys 



def check_url(url_name, tld_ex):
    #url = f"https://ipinfo.io/61.135.169.121/json?token=5a3b44c9563c04"

    try:
        url = f"https://{url_name}{tld_ex}"
        response = requests.get(url)

        if response.status_code == 200:
            #return response.url  # CN is the country code for China
            return True
        else:
            print(f"{url} - is not a valid URL")
            return False
    except:
        return False


if __name__ == "__main__":
    # Replace 'your_api_token_here' with your actual API token from IPinfo
    api_token = '5a3b44c9563c04'  
    # tld list
    tld = [".com", ".io", ".net", ".biz", ".ai", ".ru", ".cn", "uk", ".org"]

    
    # command line arg example - sys.argv
    valid_urls = []
    
    url_test_name = sys.argv[1]

    
    
    for extension in tld:
        if check_url(url_test_name, extension):
            good_url = url_test_name + extension
            valid_urls.append(good_url)



    if valid_urls:
        print("The following url names resolve")
        for ip in valid_urls:
            print(ip)
    else:
        print("No url names resolve")

# I made one change and am recommitting