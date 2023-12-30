def zero_pad_left(i):
  s = str(i)
  while len(s) < 5:
    s = "0" + s
  return s

class IntcodeComputer():
    def __init__(self, program):
        #self.mem = program 
        self.mem = {}
        counter = 0
        for byte in program:
            self.mem[counter] = byte 
            counter += 1
        self.pc = 0
        self.relative_base = 0
        self.input = []
        self.num_of_params = [-1,3,3,1,1,2,2,3,3,1]

    def set_input(self,val):
        self.input.append(val)  
    def get_input(self):
        return self.input.pop(0)
    def get_val(self,arg,mode):
        if mode == 0:
            return self.mem[arg]
        elif mode == 1:
            return arg
        elif mode == 2:
            return self.mem[self.mem[arg] + self.relative_base]
        else:
            print('invalid mode in get_val')
    def write(self,addr,val):
        self.mem[addr] = val 
    def exec(self):
        retval = 0
        while self.mem[self.pc] != 99:
            arg = [self.mem[self.pc],self.mem.get(self.pc+1),self.mem.get(self.pc+2),self.mem.get(self.pc+3)]
            if self.mem[self.pc] > 9:
                memstr = zero_pad_left(self.mem[self.pc]) 
                op = int(memstr[-2:])
                mode = [0,int(memstr[2]),int(memstr[1]),int(memstr[0])]
            else:
                op = self.mem[self.pc]
                mode = [0,0,0,0]

            if op == 1:
                p1 = self.get_val(arg[1],mode[1])
                p2 = self.get_val(arg[2],mode[2])
                self.write(arg[3],p1+p2)
                self.pc += 4
            elif op == 2:
                p1 = self.get_val(arg[1],mode[1])
                p2 = self.get_val(arg[2],mode[2])
                self.write(arg[3],p1*p2)
                self.pc += 4
            elif op == 3:
                self.write(arg[1],self.get_input())
                self.pc += 2
            elif op == 4:
                retval = self.get_val(arg[1],mode[1])
                self.pc += 2
                print("op4: ",retval)
            elif op == 5:
                if self.get_val(arg[1],mode[1]) != 0:
                    self.pc = self.get_val(arg[2],mode[2])
                else:
                    self.pc += 3
            elif op == 6:
                if self.get_val(arg[1],mode[1]) == 0:
                    self.pc = self.get_val(arg[2],mode[2])
                else:
                    self.pc += 3
            elif op == 7:
                if self.get_val(arg[1],mode[1]) < self.get_val(arg[2],mode[2]):
                    self.write(arg[3],1)
                else:
                    self.write(arg[3],0)
                self.pc += 4
            elif op == 8:
                if self.get_val(arg[1],mode[1]) == self.get_val(arg[2],mode[2]):
                    self.write(arg[3],1)
                else:
                    self.write(arg[3],0)
                self.pc += 4
            elif op == 9:
                self.relative_base += arg[1]
                self.pc += 2
        return retval, True

