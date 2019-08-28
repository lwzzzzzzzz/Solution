#!/usr/bin/python
#coding=utf-8
class Stack() :
  def __init__(self,size):
    #类的构造函数
    self.size = size
    self.stack = []

  def __str__(self):
    #类的字符串输出方法，类似于java的.toString()方法
    return str(self.stack)

  def getSize(self) :
    #获取栈当前大小
    return len(self.stack)

  def push(self, x) : #每次入栈检查栈是否满，栈满抛异常
    if self.isfull() :
      #return -1
      raise Exception("Stack is full")
    self.stack.append(x)

  def pop(self) : #每次出栈检查栈是否空，栈空抛异常
    if self.isempty() :
      raise Exception("Stack is empty")
    topElement = self.stack[-1]
    self.stack.remove(self.stack[-1])
    return topElement

  def isempty(self) :
    #判断栈空
    if len(self.stack) == 0 :
      return True
    return False

  def isfull(self) :
    #判断栈满
    if len(self.stack) == self.size :
      return True
    return False  