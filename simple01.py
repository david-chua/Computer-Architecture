PRINT_TIM         = 0b01
HALT              = 0b10
PRINT_NUM         = 0b11
SAVE              = 0b100
ADD               = 0b101
PRINT_REGISTER    = 0b110


memory = [
    PRINT_TIM,
    PRINT_NUM,
    0b01,
    PRINT_NUM,
    0b1000,
    PRINT_NUM,
    0b1111,
    PRINT_TIM,
    SAVE,
    0b1111,
    0b10,
    SAVE,
    0b1111,
    0b11,
    ADD,
    0b10,
    0b11,
    PRINT_REGISTER,
    0b10,
    PRINT_TIM,
    HALT,
]

registers = [0] * 8

running = True
pc = 0

while running:
    command = memory[pc]

    if command == PRINT_TIM:
        print("Tim!")
        pc += 1
    elif command == PRINT_NUM:
        print(memory[pc + 1])
        pc +=2
    elif command == SAVE:
        registers[memory[pc + 2]] = memory[pc + 1]
        pc +=3
    elif command == ADD:
        total = registers[memory[pc+1]] + registers[memory[pc+2]]
        registers[memory[pc+1]] = total
        pc +=3
    elif command == HALT:
        running = False

    elif command == PRINT_REGISTER:
        register_address  = memory[pc+1]
        value_to_print = registers[register_address]
        print(value_to_print)
        pc +=2
    else:
        print("I don't know what's going on")
        running = False
