import os
import getpass
import shutil
import psutil
from gpuinfo import GPUInfo

class OpSysChecker:
    def __init__(self):
        self.op_system_name = os.name
        self.user_name = getpass.getuser()
        # self.total, self.used, self.free = shutil.disk_usage("/")
        simp_list = shutil.disk_usage("/")
        self.total = simp_list[0]//(2**30)
        self.used = simp_list[1]//(2**30)
        self.free = simp_list[2]//(2**30)
        self.Gpu_is_empty = GPUInfo.get_info()
        self.Gpu_info = GPUInfo.get_info()
        self.mem = psutil.virtual_memory()
        self.mem_total = self.mem.total
        self.Virtual_memory = self.mem_total/(1024**3)

    def return_info(self):
        return_string = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.op_system_name,self.total,self.used,
                                                          self.free,self.Gpu_is_empty,self.Gpu_info,self.mem_total,
                                                          self.Virtual_memory)
        return return_string



def __main__():
    op_system_name = os.name
    op_user = getpass.getuser()
    print(op_user)
    if op_system_name == 'posix':
        print("This operating System is a Mac")
    if op_system_name == 'nt':
        print("this operating System is a Windows")
    if op_system_name == "java":
        print("this operating System is Java")
    total, used, free = shutil.disk_usage("/")
    print("Total Storage: %d GB" % (total // (2 ** 30)))
    print("Used Storage: %d GB" % (used // (2 ** 30)))
    print("Free Storage: %d GB" % (free // (2 ** 30)))
    print("cpu percentage = {}\nVirtual Storage = {}".format(psutil.cpu_percent(),psutil.virtual_memory()))
    for each in psutil.virtual_memory():
        print(each)
    print('memory % used:', psutil.virtual_memory()[2])
    print(GPUInfo.check_empty())
    print(GPUInfo.get_info())
    print(GPUInfo.gpu_usage())
    mem = psutil.virtual_memory()
    print(mem.total)
    print("Ram = {}".format(mem.total/1024.**3))
    op_check = OpSysChecker()
    print("-----------------\n{}".format(op_check.return_info()))

if __name__ == '__main__':
   __main__()