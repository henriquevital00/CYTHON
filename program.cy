number resultado;
number j = 1;
number i = 1;
str help = "prof, da 10 ai";

print("Ate qual numero voce quer a tabuada?");
number limit = input();


while limit == 0 {
    print("Digite um numero maior que zero");
    limit = input();

    if limit == 0 {
        print("");
        print("para de digitar zero, amigao");
    };
     else {
        print("Calculando a tabuada...");
    };
};

while i <= limit {
    j = 0;

    print("");
    print("TABUADA");
    print(i);
    print("");

    while j <= 10 {
        resultado = j * i;
        print(resultado);
        j = j + 1;
    };

    i = i + 1;

    if i > limit {
        print(help);
    };
};