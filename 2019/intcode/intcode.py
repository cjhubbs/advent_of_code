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
    def exec(self):
        retval = 0
        while self.mem[self.pc] != 99:
            p = [-1,-1,-1,-1]
            if self.mem[self.pc] > 9:
                memstr = zero_pad_left(self.mem[self.pc]) 
                op = int(memstr[-2:])
                mode = [0,memstr[2],memstr[1],memstr[0]]
                
                for i in range(1,self.num_of_params[op]):
                    if mode[i] == "0":
                        p[i] = self.mem[self.mem[self.pc+i]]
                    elif mode[i] == "1":
                        p[i] = self.mem[self.pc+i]
                    elif mode[i] == "2":
                        p[i] = self.mem[self.mem[self.pc+i] + self.relative_base]
                    else:
                        print("error in memory addressing")
                p[3] = self.mem[self.pc+3]
                if mode[3] == "2":
                    p[3] += self.relative_base
            else:
                op = self.mem[self.pc]
                p[1] = self.mem[self.mem[self.pc+1]]
                if self.num_of_params[op] > 1:
                    p[2] = self.mem[self.mem[self.pc+2]]
                if self.num_of_params[op] > 2:
                    p[3] = self.mem[self.pc+3] 
            if op == 1:
                self.mem[p[3]] = p[1]+p[2]
                self.pc += 4
            elif op == 2:
                self.mem[p[3]] = p[1]*p[2]
                self.pc += 4
            elif op == 3:
                self.mem[self.mem[self.pc+1]] = self.get_input()
                self.pc += 2
            elif op == 4:
                #print("op4 output = ",p1)
                self.pc += 2
                retval = p[1]
                return retval, False
            elif op == 5:
                if p[1] != 0:
                    self.pc =  p[2]
                else:
                    self.pc += 3
            elif op == 6:
                if p[1] == 0:
                    self.pc = p[2]
                else:
                    self.pc += 3
            elif op == 7:
                if p[1] < p[2]:
                    self.mem[p[3]] = 1
                else:
                    self.mem[p[3]] = 0
                self.pc += 4
            elif op == 8:
                if p[1] == p[2]:
                    self.mem[p[3]] = 1
                else:
                    self.mem[p[3]] = 0
                self.pc += 4
            elif op == 9:
                self.relative_base += p[1]
                self.pc += 2
        return retval, True

