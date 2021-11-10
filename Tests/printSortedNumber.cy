number fisrt_number;
number second_number;
number third_number;

print("Digite o 1 numero:");
fisrt_number = input();
print("Digite o 2 numero:");
second_number = input();
print("Digite o 3 numero:");
third_number = input();

if fisrt_number > second_number & second_number > third_number{
    print(fisrt_number);
    print(second_number);
    print(third_number);
};
elif fisrt_number > third_number & third_number > second_number {
    print(fisrt_number);
    print(third_number);
    print(second_number);
};
elif second_number > fisrt_number & fisrt_number > third_number {
    print(third_number);
    print(fisrt_number);
    print(second_number);
};
elif second_number > third_number & third_number > fisrt_number {
    print(second_number);
    print(third_number);
    print(fisrt_number);
};
elif third_number > second_number & second_number > fisrt_number {
    print(third_number);
    print(second_number);
    print(fisrt_number);
};
elif third_number > fisrt_number & fisrt_number > second_number {
    print(third_number);
    print(fisrt_number);
    print(second_number);
};