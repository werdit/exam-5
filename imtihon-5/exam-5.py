# import asyncio
# import json
# import os
#
# import httpx
# import requests
#
#
# class FileManager:
#     def __init__(self, file_path, mode):
#         self.file_path = file_path
#         self.mode=mode
#
#     def __iter__(self):
#         self.file = open(file=self.file_path, mode=self.mode)
#         return self
#
#     def __next__(self):
#         data=self.file.mode
#         if not data:
#             self.file.close()
#             raise StopIteration
#         return data.strip()
#
#
# if __name__ == '__main__':
#     fruits = []
#     for file in os.listdir(f'C:/Users/user/Downloads/Telegram Desktop/exam5/descriptions'):
#         data ={}
#         file_data = []
#         for line in FileManager(f"C:/Users/user/Downloads/Telegram Desktop/exam5/descriptions/{file}", 'r'):
#             file_data = line.split("\n")
#         data["name"]=file_data[0]
#         data["price"]=int(file_data[1].split()[0])
#         data["description"] = file_data[2]
#         fruits.append(data)
#         file_data.clear()
#         print(fruits)
#     url='http://164.92.64.76/desc/'
#     response=requests.get(url)
#     data=response.json()
#     with open('response.txt', 'w') as f:
#         f.write(f'Response {data.status_code}')
from multithreading.multithread import Thread

#2-masala
@printer
def teskari(a:int):
    z=str(a)
    d=z[::-1]
    s=int(d)
    return s

def print_teskari(b:list):
    w=[]
    for i in b:
        f=teskari(i)
        w.append(f)
    return f

def printer(func):
    def inner(*args, **kwargs):
        args=(args)
        print(func)
    return inner

if __name__ == '__main__':
    g=list(map(int, input("input numbers: ").split()))
    t=Thread(target=teskari, args=(g,))
    t.start()
    t.join()




