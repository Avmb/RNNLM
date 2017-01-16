#! /usr/bin/python

import codecs
import sys

utf8Reader = codecs.getreader('utf8')
utf8Writer = codecs.getwriter('utf8')
sys.stdin = utf8Reader(sys.stdin)
sys.stdout = utf8Writer(sys.stdout)

def main():
	for line in sys.stdin:
                words = line.split()
                all_toks = []
                for w in words:
                        if w == "<unk>":
                        	toks = ['<unk>']
                        else:
				toks = [tok for tok in w]
                        if len(all_toks) > 0:
                        	all_toks.append('SP')
                        all_toks.extend(toks)
		print ' '.join(all_toks)

if __name__ == '__main__':
	main()


