class Assembly_Runner:
    def __init__(self):
        self.asm_codes = []
        self.regs = [None]*32
        self.read_file()
    def read_file(self):
        file = open("asm.txt",mode="r")
        self.asm_codes = file.read().splitlines()
    def run(self):
        for code in self.asm_codes:
            code_sections = code.split(" ")
            if code_sections[0] == "MOV":
                self.mov(code_sections[1],code_sections[2])
            elif code_sections[0] == "ADD":
                self.add(code_sections[1],code_sections[2])
            elif code_sections[0] == "SUB":
                self.sub(code_sections[1],code_sections[2])
            elif code_sections[0] == "DIV":
                self.div(code_sections[1],code_sections[2])
            elif code_sections[0] == "MUL":
                self.mul(code_sections[1],code_sections[2])

    def mov(self,a,b):
        reg_index = int(a[1:])
        data = float(b)
        self.regs[reg_index] = data
    def add(self,a,b):
        reg_index_1 = int(a[1:])
        reg_index_2 = int(b[1:])
        self.regs[reg_index_1] += self.regs[reg_index_2]
    def sub(self,a,b):
        reg_index_1 = int(a[1:])
        reg_index_2 = int(b[1:])
        self.regs[reg_index_1] -= self.regs[reg_index_2]
    def div(self,a,b):
        reg_index_1 = int(a[1:])
        reg_index_2 = int(b[1:])
        self.regs[reg_index_1] /= self.regs[reg_index_2]
    def mul(self,a,b):
        reg_index_1 = int(a[1:])
        reg_index_2 = int(b[1:])
        self.regs[reg_index_1] *= self.regs[reg_index_2]

def main():
    asm_runner = Assembly_Runner()
    print("registers")
    print(asm_runner.regs)
