printf("Digite o 1 numero:");
number first_number = inputf();
printf("Digite a operacao:");
str operation = inputf();
printf("Digite o 2 numero:");
number second_number = inputf();
number result;


if operation == "+"{
    result = first_number + second_number;
    printf(result);
};
elif operation == "-"{
    result = first_number - second_number;
    printf(result);
};
elif operation == "/"{
    result = first_number / second_number;
    printf(result);
};
elif operation == "*"{
    result = first_number * second_number;
    printf(result);
};
else{
    printf("Voce fez coisa errada");
};