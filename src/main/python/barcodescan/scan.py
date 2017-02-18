import sys
import logging
import httplib2


def scan():
  logging.info("scaning ... ")
  h = httplib2.Http(".cache")
  resp, content = h.request("http://heise.de/", "GET")
  print(resp.status)
  print(content)


def main():
  logging.basicConfig(level=logging.INFO)
  scan()

if __name__ == '__main__':
  main()