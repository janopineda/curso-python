import subprocess

#subprocess.call(["copy","con","pollo.txt"],shell=True)
subprocess.run('echo Hola > nopal.txt', shell=True)
subprocess.call(["mkdir","Tomate"],shell=True)
subprocess.call(["del","Tomate"],shell=True)
subprocess.call(["del","nopal.txt"],shell=True)