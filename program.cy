number resultado;
number j = 1;
number i = 1;
str help = "prof, da 10 ai";

print("Ate qual numero voce quer a tabuada?");
number limit = input();

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