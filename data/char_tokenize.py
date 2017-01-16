#! /usr/bin/python

import codecs
import sys

utf8Reader = codecs.getreader('utf8')
utf8Writer = codecs.getwriter('utf8')
sys.stdin = utf8Reader(sys.stdin)
sys.stdout = utf8Writer(sys.stdout)

def main():
	for line in sys.stdin:
		toks = [(tok if not tok.isspace() else 'SP') for tok in line.strip()]
		print ' '.join(toks)

if __name__ == '__main__':
	main()


