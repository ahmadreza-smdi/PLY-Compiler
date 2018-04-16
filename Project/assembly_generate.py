class Assembly_Generator:

    def init(self):
        self.out = [];
        self.regs = [None]*32;


    def mov(self,b):
        # اولین رجیستر خالی
        free_reg_indea = self.regs.indea(None);
        self.regs[free_reg_indea] = 1;
        command = "MOV R"+str(free_reg_indea)+" "+ str(b);
        self.out.append(command);
        return free_reg_indea;


    def sub(self ,a ,b):
        self.out.append("SUB R"+str(a)+" R"+str(b));

    def add(self ,a ,b):
        self.out.append("ADD R"+str(a)+" R"+str(b));

    def mul(self ,a ,b):
        self.out.append("MUL R"+str(a)+" R"+str(b));

    def div(self ,a ,b):
        self.out.append("DIV R"+str(a)+" R"+str(b));


    def write2file(self):
        statement='' ;
        file = open("asm.txt","w+");
        for i in range(len(self.out)):
            statement += self.out[i] + '\n';

        file.write(statement);
        
        file.close;