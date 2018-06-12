#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Jerod Gawne, 2017-10-05

Text Wrap

https://www.hackerrank.com/challenges/text-wrap/

Editorial:
 -This can be solved using the function textwrap.fill().
"""
import textwrap
import string, re
import argparse
import os.path
import sys, getopt

def indent(text, prefix, predicate=None):
    """Adds 'prefix' to the beginning of selected lines in 'text'.

    If 'predicate' is provided, 'prefix' will only be added to the lines
    where 'predicate(line)' is True. If 'predicate' is not provided,
    it will default to adding 'prefix' to all non-empty lines that do not
    consist solely of whitespace characters.
    """
    if predicate is None:
        def predicate(line):
            return line.strip()

    def prefixed_lines():
        for line in text.splitlines(True):
            yield (prefix + line if predicate(line) else line)
    return ''.join(prefixed_lines())

def auto_wrap(input_file, dst_file, width):
	
    finput=open(input_file, "r")
    alllines=finput.readlines()
    finput.close()
    foutput = 0
    flag_add = 0
    pos = 0
    output_file = dst_file
    foutput = open(output_file, 'a')
    for eachline in alllines:
        pos = eachline.rstrip('\\\n').rfind('\\',0,width)
        if (pos == width-1) :
            bc = textwrap.fill(eachline,pos-1)
            print("backslash appear at the end of the line, the line is\
                  wrapped at the position one character before the backslash")
        else :
            bc = textwrap.fill(eachline,73)
        tmplines = bc.split('\n')
        tmplen = len(tmplines)
        if tmplen == 1 :
            foutput.writelines(bc)
            foutput.writelines('\n')
        else :
            flag_add = 0
            i = 0
            while i < tmplen-1 :
                if(flag_add == 1) :
                    tmplines[i] = indent(tmplines[i], '  ')
                foutput.writelines(tmplines[i])
                foutput.writelines('\\')
                flag_add = 1
                foutput.writelines('\n')
                i += 1
                if(flag_add == 1) :
                    tmplines[i] = indent(tmplines[i], '  ')
                foutput.writelines(tmplines[tmplen-1])
                foutput.writelines('\n')
    foutput.close

def auto_unwrap(input_file, dst_file) :
    finput=open(input_file, "r")
    alllines=finput.readlines()
    finput.close()
    foutput = 0
    flag_del = 0
    flag_space = 0 
    output_file = dst_file
    foutput = open(output_file, 'a')
    for eachline in alllines:
        print(eachline)
        if(flag_del == 1) :
            eachline = eachline[2:]
        if eachline.endswith('\\\n') :
            flag_del = 1
            eachline = eachline.rstrip('\\\n')
            if eachline == '':
                flag_del = 0
        else :
            flag_del = 0
        if eachline == '\n' :
            continue
        foutput.writelines(eachline)


"""	
    for eachline in alllines:
        bc = eachline.split('\\')
        if(flag_del == 1) :
            foutput.writelines(bc[0][2:])
        else :
            foutput.writelines(bc[0])
        if len(bc) == 1 :
            flag_del = 0
        else :
            flag_del = 1
"""

"""
def auto_unwrap(input_file, dst_file) :
    finput=open(input_file, "r")
    alllines=finput.readlines()
    finput.close()
    foutput = 0
    flag_del = 0
    flag_enter = 0 
    output_file = dst_file
    foutput = open(output_file, 'a')
    for eachline in alllines:
        #bc = eachline.split('\\')
        #print(bc)
        if eachline.endswith('\\\n') :
            flag_del = 1
            eachline = eachline.strip('\\\n')
        else :
            flag_del = 0
        bc = eachline
        print(bc)
        #print(eachline.endswith("\\\n"))
        #print(eachline)
        if(flag_del == 1) :
            foutput.writelines(bc[2:])
        else:
            foutput.writelines(bc)
"""

if __name__ == "__main__":
    #print textwrap.dedent("\tfoo\n\tbar")
    #print textwrap.dedent("  \thello there\n  \t  how are you?")
    print(textwrap.dedent("Hello there.\n  This is indented."))
    print(indent("Hello there.",'  '))
    auto_wrap("abc.txt","abcd2.txt",73)
    auto_unwrap("abcd2.txt", "abc2.txt")
    print("Hello there..\\".rstrip('\\'))
