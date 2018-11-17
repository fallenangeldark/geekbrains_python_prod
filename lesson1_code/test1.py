import subprocess

args = ["ping", "www.youtube.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE, encoding='cp866')
data = process.communicate()
for el in data:
    if el != None:
        print(el, end='\n')
    #Отсекаем stderr
    continue


code = subprocess.call("notepad.exe")
if code == 0:
    print("Success!")
else:
    print("Error!")
