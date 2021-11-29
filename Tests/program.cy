number resultado;
number j = 1;
number i = 1;
str help = "prof, da 10 ai";

print("Ate qual numero voce quer a tabuada?");
number limit = inputf();


while limit == 0 {
    printf("Digite um numero maior que zero");
    limit = inputf();

    if limit == 0 {
        printf("");
        printf("para de digitar zero, amigao");
    };
     else {
        printf("Calculando a tabuada...");
    };
};

while i <= limit {
    j = 0;

    printf("");
    printf("TABUADA");
    printf(i);
    printf("");

    while j <= 10 {
        resultado = j * i;
        printf(resultado);
        j = j + 1;
    };

    i = i + 1;

    if i > limit {
        printf(help);
    };
};
