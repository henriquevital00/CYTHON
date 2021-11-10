print("Digite o 1 numero:");
number first_number = input();
print("Digite a operacao:");
str operation = input();
print("Digite o 2 numero:");
number second_number = input();
number result;


if operation == "+"{
    result = first_number + second_number;
    print(result);
};
elif operation == "-"{
    result = first_number - second_number;
    print(result);
};
elif operation == "/"{
    result = first_number / second_number;
    print(result);
};
elif operation == "*"{
    result = first_number * second_number;
    print(result);
};
else{
    print("Voce fez coisa errada");
};