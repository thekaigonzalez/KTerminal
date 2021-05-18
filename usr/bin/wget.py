import requests

def main(s,a,c,o):
    if c == 0:
        s.addstr("missing (url).\n")
    elif c == 1:
        s.addstr("getting " + a[0] + "\n")
        s.addstr("download " + a[0] + "\n")
        re = requests.request('GET', a[0])
        if (re.status_code == 404):
            s.addstr("download failed: server responded with code 400.\n")
        elif re.status_code == 200:
            s.addstr("download success: server responded with code 200.\n")

            bb = re.url

            fname = bb[bb.rfind('/')+1:len(bb)]

            s.addstr("creating file " + fname + "\n")
            y = open(o[4] + "/" + fname , 'w')
            y.write(re.text)
            y.close()