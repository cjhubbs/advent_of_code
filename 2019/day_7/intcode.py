def zero_pad_left(i):
  s = str(i)
  while len(s) < 5:
    s = "0" + s
  return s

class IntcodeComputer():
    def __init__(self, program):
        self.mem = program 
        self.pc = 0
        self.input = []
        self.num_of_params = [-1,3,3,1,1,2,2,3,3]

    def set_input(self,val):
        self.input.append(val)  
    def get_input(self):
        return self.input.pop(0)
    def exec(self):
        retval = 0
        while self.mem[self.pc] != 99:
            #print("pc = ",self.pc)
            if self.mem[self.pc] > 8:
                memstr = zero_pad_left(self.mem[self.pc]) 
                op = int(memstr[-2:])
                mode1 = memstr[2]
                mode2 = memstr[1]
                
                p1 = 0
                p2 = 0
                p3 = self.mem[self.pc+3]
                if mode1 == "0":
                    p1 = self.mem[self.mem[self.pc+1]]
                else:
                    p1 = self.mem[self.pc+1]
                if self.num_of_params[op] > 1:
                    if mode2 == "0":
                        p2 = self.mem[self.mem[self.pc+2]]
                    else:
                        p2 = self.mem[self.pc+2]
            else:
                op = self.mem[self.pc]
                p1 = self.mem[self.mem[self.pc+1]]
                if self.num_of_params[op] > 1:
                    p2 = self.mem[self.mem[self.pc+2]]
                if self.num_of_params[op] > 2:
                    p3 = self.mem[self.pc+3]
            if op == 1:
                self.mem[p3] = p1+p2
                self.pc += 4
            elif op == 2:
                self.mem[p3] = p1*p2
                self.pc += 4
            elif op == 3:
                self.mem[self.mem[self.pc+1]] = self.get_input()
                self.pc += 2
            elif op == 4:
                #print("op4 output = ",p1)
                self.pc += 2
                retval = p1
                return p1, False
            elif op == 5:
                if p1 != 0:
                    self.pc =  p2
                else:
                    self.pc += 3
            elif op == 6:
                if p1 == 0:
                    self.pc = p2
                else:
                    self.pc += 3
            elif op == 7:
                if p1 < p2:
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                self.pc += 4
            elif op == 8:
                if p1 == p2:
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                self.pc += 4
        return retval, True

