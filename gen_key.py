'''Write a function called gen_key that creates a license key with this format: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

The key consists of a combination of upper case letters and digits.'''

def gen_key():
        length = 32
        characters = string.ascii_letters + string.digits
        new_key = ''.join(secrets.choice(characters) for _ in range(length))
        new_key = new_key.upper()
        separator = "-"
        res = ""
        for i in range(0, length-1,8):
            res += new_key[i:i+8] + separator
        res = res[:-1]
        return res
        print("The generated random string: "+str(res))

def gen_key(parts=4, chars_per_part=8):
        length = parts*chars_per_part
        characters = string.ascii_letters + string.digits
        new_key = ''.join(secrets.choice(characters) for _ in range(length))
        new_key = new_key.upper()
        separator = "-"
        res = ""
        for i in range(0, length-1,chars_per_part):
            res += new_key[i:i+chars_per_part] + separator
        res = res[:-1]
        return res
        print("The generated random string: "+str(res))
    
