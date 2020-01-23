class Intcode():
    def __init__(self, inputs):
        self.data = inputs
        self.original_data = inputs
        self.current_position = 0
        self.opcode = 0
        self.par1 = 0
        self.par2 = 0
        self.par3 = 0
        self.relative_base = 0
        self.outputs = []

    def parse_opcode(self, x):
        try:
            self.par1 = int(str(x)[-3])
        except:
            self.par1 = 0
        try:
            self.par2 = int(str(x)[-4])
        except:
            self.par2 = 0
        try:
            self.par3 = int(str(x)[-5])
        except:
            self.par3 = 0
        self.opcode = x % 100

    def translate_pars(self):
        if self.par1 == 0:
            self.par1 = self.data[self.current_position +1]
        else:
            if self.par1 == 1:
                self.par1 = self.current_position +1
            else:
                par = self.relative_base + self.data[self.current_position +1]
                self.par1 = par
        if self.par2 == 0:
            self.par2 = self.data[self.current_position + 2]
        else:
            if self.par2 == 1:
                self.par2 = self.current_position +2
            else:
                par = self.relative_base + self.data[self.current_position +2]
                self.par2 = par
        if self.par3 == 0:
            self.par3 = self.data[self.current_position+3]
        else:
            if self.par3 == 1:
                self.par3 = self.current_position + 3
            par = self.relative_base + self.data[self.current_position +3]
            self.par3 = par

    def do_instructions(self):
        # add
        if self.opcode == 1:
            self.data[self.par3] = self.data[self.par1] + self.data[self.par2]
            self.current_position += 4
        # multiply
        if self.opcode == 2:
            self.data[self.par3] = self.data[self.par1] * self.data[self.par2]
            self.current_position += 4
        # input instruction
        if self.opcode == 3:
            input_a = self.get_input()
            self.data[self.par1] = input_a
            self.current_position += 2
        # output instruction
        if self.opcode == 4:
            print(self.data[self.par1])
            self.outputs.append(self.data[self.par1])
            self.current_position += 2
        # finish program
        if self.opcode == 99:
            self.current_position = -1
            return self.data
        # jump-if-true (non-zero)
        if self.opcode == 5:
            if self.data[self.par1] != 0:
                self.current_position = self.data[self.par2]
            else:
                self.current_position += 3
        # jump-if-false (zero)
        if self.opcode == 6:
            if self.data[self.par1] == 0:
                self.current_position = self.data[self.par2]
            else:
                self.current_position += 3
        # less than
        if self.opcode == 7:
            if self.data[self.par1] < self.data[self.par2]:
                self.data[self.par3] = 1
            else:
                self.data[self.par3] = 0
            self.current_position += 4
        # equals
        if self.opcode == 8:
            if self.data[self.par1] == self.data[self.par2]:
                self.data[self.par3] = 1
            else:
                self.data[self.par3] = 0
            self.current_position += 4
        # adjusts relative base
        if self.opcode == 9:
            self.relative_base += self.data[self.par1]
            self.current_position += 2

    def get_input(self):
        return 0

    def run(self):
        # fetch -> decode -> get_args -> execute
        while self.current_position >= 0:
            self.parse_opcode(self.data[self.current_position])
            if self.opcode != 99:
                self.translate_pars()
            self.do_instructions()

