
printf("Digite o 1 numero:");
number fisrt_number = inputf();
printf("Digite o 2 numero:");
number second_number = inputf();
printf("Digite o 3 numero:");
number third_number = inputf();

str a = inputf();

if fisrt_number > second_number & second_number > third_number{
    printf(fisrt_number);
    printf(second_number);
    printf(third_number);
};
elif fisrt_number > third_number & third_number > second_number {
    printf(fisrt_number);
    printf(third_number);
    printf(second_number);
};
elif second_number > fisrt_number & fisrt_number > third_number {
    printf(third_number);
    printf(fisrt_number);
    printf(second_number);
};
elif second_number > third_number & third_number > fisrt_number {
    printf(second_number);
    printf(third_number);
    printf(fisrt_number);
};
elif third_number > second_number & second_number > fisrt_number {
    printf(third_number);
    printf(second_number);
    printf(fisrt_number);
};
elif third_number > fisrt_number & fisrt_number > second_number {
    printf(third_number);
    printf(fisrt_number);
    printf(second_number);
};