import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = 'a17V0RN9ZyyBVF6jkcDa_CEMx38RiBdw'
def main():
   paste_url =  post_new_paste('', '', '', '')

def post_new_paste(title, body_text, expiration='10M', listed=True):
    """Creates a new Paste bin paste

    Args:
        title (ste): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last. (See https://pastebin.com/doc_api) Defaults to '10m'.
        listed (bool, optional): whether the post is listed or not. Defaults to True.

    Returns:
        Str of Pastebin URL if successful. None if  not
    """
    params = {
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }

    print('Posting new paste to Pastbin...', end='')
    resp_msg = requests.post(API_POST_URL, data=params)
    
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        
        return resp_msg.text
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return
    

if __name__=="__main__":
    main()