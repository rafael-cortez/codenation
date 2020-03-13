from json import dumps
from requests import get, post
from hashlib import sha1


def decrypt(encrypted, number):
    encrypted = encrypted.lower()
    decrypted_text = str()
    for l in encrypted:
        if 97 <= ord(l) <= 122:
            decrypted_text += chr(122 - ((122 - ord(l) + number) % 26))
            continue
        decrypted_text += l
    return decrypted_text


def save_json(decrypted_text):
    data = json_origin
    data['decifrado'] = decrypted_text
    data['resumo_criptografico'] = sha1(text.encode('utf-8')).hexdigest()
    with open('answer.json', 'w') as j:
        j.write(dumps(data))


## Variables declaration
token = '259c8433cbaf4745799b581fd11de43df5dc73a4'
url_destiny = f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={token}'
url_origin = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}'

## Get Json
response = get(url_origin)
json_origin = response.json()

## Decrypt text and save as JSON
text = decrypt(json_origin['cifrado'], json_origin['numero_casas'])
save_json(text)

## Send the answer for validation
response = post(url_destiny, files={'answer': ('answer.json', open('answer.json', 'rb'))})
print(response.text)
