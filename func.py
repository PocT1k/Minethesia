# UTF-8 Будет здесь!

import chardet


def decodStr(inStr):
    byte_data = inStr.encode('latin1')  # Используем 'latin1' как универсальную кодировку для начала
    result = chardet.detect(byte_data)
    encoding = result['encoding']

    try: return byte_data.decode(encoding, errors='replace')
    except (TypeError, ValueError): return byte_data.decode('utf-8', errors='replace')
pass #funck decodStr()
