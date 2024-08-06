
import pytest
import myModule
import unittest
from Calculator import Add,Multiply
def add(a, b):
    return a + b
def multiply(a,b):
    return a*b


def test_add():
 assert add(1,2)==3
 assert add(1,1)==2
 assert add(1,-1)==0
 
def test_multiply():
 assert multiply(1,2)==2
 assert multiply(1,1)==1
 assert multiply(1,-1)==-1