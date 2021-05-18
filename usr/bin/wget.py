import requests

def main(s,a,c,o):
    if c == 0:
        s.addstr("missing (url).\n")
    elif c == 1:
        s.addstr("getting " + a[0])
        s.addstr("download " + a[0])
        re = requests.request('GET', a[0])
        if (re.status_code == 400):
            s.addstr("download failed: server responded with code 400.\n")
        elif re.status_code == 200:
            s.addstr("download success: server responded with code 200.\n")
            stri = a[0]
            bb = str(stri)

            fname = bb[bb.find('/')+1:len(bb)]

            s.addstr("creating file " + fname + "\n")
            y = open(fname , 'w')
            y.write(re.text)
            y.close()