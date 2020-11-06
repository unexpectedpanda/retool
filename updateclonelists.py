import hashlib
import json
import os
import socket
import time
import urllib.parse
import urllib.request


def main():
    print('\n* Checking online for clone list updates... ')

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request('https://raw.githubusercontent.com/unexpectedpanda/retool/master/clonelists/hash.json', None, headers)
    page = get_page(req)

    file_count = 0

    # Create folders if they're missing
    if not os.path.exists(os.path.abspath('clonelists')):
        os.mkdir('clonelists')
    if not os.path.exists(os.path.abspath('metadata')):
        os.mkdir('metadata')

    for key, value in json.loads(page).items():
        if os.path.exists(os.path.abspath('clonelists/' + key)) == True:
            hash_md5 = hashlib.md5()

            with open (os.path.abspath('clonelists/' + key), 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_md5.update(chunk)
                file.close()

            if hash_md5.hexdigest() != value:
                file_count += 1
                print(f'* Found an update for {key}. Downloading...')
                req = urllib.request.Request(f'https://raw.githubusercontent.com/unexpectedpanda/retool/master/clonelists/{urllib.parse.quote(key)}', None, headers)
                page = get_page(req)

                with open (os.path.abspath('clonelists/' + key), 'wb') as output_file:
                    output_file.write(page)

        else:
            file_count += 1
            print(f'  * Found a new clone list, {key}. Downloading...')
            req = urllib.request.Request(f'https://raw.githubusercontent.com/unexpectedpanda/retool/master/clonelists/{urllib.parse.quote(key)}', None, headers)
            page = get_page(req)

            with open (os.path.abspath('clonelists/' + key), 'wb') as output_file:
                output_file.write(page)

    print('* Checking online for metadata updates... ')

    req = urllib.request.Request('https://raw.githubusercontent.com/unexpectedpanda/retool/master/metadata/hash.json', None, headers)
    page = get_page(req)

    for key, value in json.loads(page).items():
        if os.path.exists(os.path.abspath('metadata/' + key)) == True:
            hash_md5 = hashlib.md5()

            with open (os.path.abspath('metadata/' + key), 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_md5.update(chunk)
                file.close()

            if hash_md5.hexdigest() != value:
                file_count += 1
                print(f'* Found an update for {key}. Downloading...')
                req = urllib.request.Request(f'https://raw.githubusercontent.com/unexpectedpanda/retool/master/metadata/{urllib.parse.quote(key)}', None, headers)
                page = get_page(req)

                with open (os.path.abspath('metadata/' + key), 'wb') as output_file:
                    output_file.write(page)

        else:
            file_count += 1
            print(f'  * Found a new metadata file, {key}. Downloading...')
            req = urllib.request.Request(f'https://raw.githubusercontent.com/unexpectedpanda/retool/master/metadata/{urllib.parse.quote(key)}', None, headers)
            page = get_page(req)

            with open (os.path.abspath('metadata/' + key), 'wb') as output_file:
                output_file.write(page)

    if file_count == 0:
        print('* Done. No new updates are available.')
    elif file_count == 1:
        print(f'* Done. Downloaded {file_count} file.')
    else:
        print(f'* Done. Downloaded {file_count} files.')


def get_page(req):
    retrieved = False

    while retrieved == False:
        try:
            with urllib.request.urlopen(req) as response:
                page = response.read()
        except HTTPError as error:
            now = datetime.now()
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Data not retrieved', error, req)
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Skipping...')
            retrieved = True
        except URLError as error:
            now = datetime.now()
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something unexpected happened: {error}')
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...')
            time.sleep(5)
        except socket.error as error:
            now = datetime.now()
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket error: {error}')
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...')
            time.sleep(5)
        except socket.timeout as error:
            now = datetime.now()
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Socket error: {error}')
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Trying again in 5 seconds...')
            time.sleep(5)
        except:
            now = datetime.now()
            print(f'* [{now.strftime("%m/%d/%Y, %H:%M:%S")}]: Something even more unexpected happened: {error}')
            print(f'Trying again in 5 seconds...')
            time.sleep(5)
        else:
            retrieved = True

    return page


if __name__ == '__main__':
    main()