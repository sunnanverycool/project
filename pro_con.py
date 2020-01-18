import queue
import time
import threading
table=queue.Queue(50)
a=0
def dad(table,t):
    while 1:
        time.sleep(t)
        table.put("满汉全席")
        print("爸爸做了一份满汉全席，现在有",table.qsize(),"份满汉全席等待着我们！")
def mom(table,t):
    while 1:
        time.sleep(t)
        table.put("满汉全席")
        print("妈妈做了一份满汉全席，现在有",table.qsize(),"份满汉全席等待着我们！")

def wo(table,t):
    while 1:
        time.sleep(t)
        table.get()
        print("满汉全席被(我)吃掉了一份！我们只剩下",table.qsize(),"份满汉全席了！")
def gege(table,t):
    while 1:
        a=0
        time.sleep(t)
        for i in range(5):
            table.get()
            if table.empty():
                print("满汉全席被(我哥)吃掉了",i+1,"份！我们只剩下", table.qsize(), "份满汉全席了！")
                a=1
                break
        if a==0:
            print("满汉全席被(我哥)吃掉了5份！我们只剩下", table.qsize(), "份满汉全席了！")

def tongxue(table,t):
    while 1:
        b=0
        time.sleep(t)
        for i in range(10):
            table.get()
            if table.empty():
                print("满汉全席被我路过的同学们吃掉了",i+1,"份！我们只剩下", table.qsize(), "份满汉全席了！")
                b=1
                break
        if b==0:
            print("满汉全席被我路过的同学们吃掉了整整10份！我们只剩下", table.qsize(), "份满汉全席了！")


p1 = threading.Thread(target=dad,args=[table, 2.4])
p2 = threading.Thread(target=mom,args=[table, 1.9])

p1.start()
p2.start()

p3 = threading.Thread(target=wo,args=[table, 2.2])
p4= threading.Thread(target=gege,args=[table, 12])
p5= threading.Thread(target=tongxue,args=[table, 80])
p3.start()
p4.start()
p5.start()