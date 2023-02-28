let figura = prompt(
  "introduce la figura a calcular : cuadrado,rectangulo,triangulo,circulo, rombo, esfera,prisma,cubo,piramide"
);
let base;
let altura;
let area;
let radio;
let Diagonalmenor;
let diagonalmayor;
let perimetro;
let Lado = 0;
let Lado2 = 0;
let Lado3 = 0;
let volumen;

switch (figura) {
  case "triangulo":
    base = prompt("ingrese la base");
    altura = prompt("ingrese la altura");
    lado = prompt("ingrese el lado 1");
    lado2 = prompt("ingrese el lado 2");
    area = (base * altura) / 2;
    perimetro = parseInt(base) + parseInt(lado) + parseInt(lado2);

    window.alert("el area de el triangulo es  " + area);
    window.alert("el perimetro del triangulo es " + perimetro);
    break;

  case "cuadrado":
    base = prompt("ingrese la base");
    altura = prompt("ingrese la altura");
    area = base * altura;
    perimetro =
      parseInt(base) + parseInt(base) + parseInt(altura) + parseInt(altura);
    window.alert("el area del cuadrado es" + area);
    window.alert("el perimetro del cuadrado es" + perimetro);
    break;

  case "rectangulo":
    base = prompt("ingrese la base");
    altura = prompt("ingrese la altura");
    area = base * altura;
    perimetro =
      parseInt(base) + parseInt(base) + parseInt(altura) + parseInt(altura);
    window.alert("el area del rectangulo es" + area);
    window.alert("el perimetro del rectangulo es" + perimetro);
    break;

  case "circulo":
    radio = prompt("ingrese el radio");

    area = radio * radio * 3.14;
    perimetro = 3.14 * 2 * radio;
    window.alert("el area de el circulo es  " + area);
    window.alert("el perimetro del circulo es " + perimetro);
    break;

  case "rombo":
    Diagonalmenor = prompt("Ingrese la Diagonal menor");
    diagonalmayor = prompt("ingrese la diagonal mayor");
    lado = prompt("ingrese el lado del rombo");

    area = (diagonalmayor * Diagonalmenor) / 2;
    perimetro = lado * 4;
    window.alert("el area del rombo es  " + area);
    window.alert("el perimetro del rombo es " + perimetro);
    break;

  case "esfera":
    radio = prompt("ingrese el radio");
    area = (4 * 3, 14 * radio * radio);
    volumen = (4 / 3) * 3.14 * radio * radio * radio;

    window.alert(" el area de la esfera es " + area);
    window.alert("el volumen de la esfera es" + volumen);
    break;

  case "prisma":
    Lado = prompt("ingrese el Lado 1");
    Lado2 = prompt("ingrese el Lado 2");
    Lado3 = prompt("ingrese el lado 3");
    area =
      parseInt(Lado) +
      parseInt(Lado) +
      parseInt(Lado2) +
      parseInt(Lado2) +
      parseInt(Lado) +
      parseInt(Lado) +
      parseInt(Lado3) +
      parseInt(Lado3) +
      parseInt(Lado2) +
      parseInt(Lado2) +
      parseInt(Lado3) +
      parseInt(Lado3);
    volumen = Lado * Lado2 * Lado3;

    window.alert("el area del prisma es" + area);
    window.alert("el volumen del prismaes" + volumen);
    break;

  case "cubo":
    Lado = prompt("ingrese el lado del cubo");

    area = 6 * Lado * Lado;
    volumen = Lado * Lado * Lado;

    window.alert("el area del cubo es" + area);
    window.alert("el volumen del cubo es " + volumen);
    break;

  case "piramide":
    Lado = prompt("ingrese el lado de la piramide");
    altura = prompt("ingrese la altura de la piramide");

    area = Lado * Lado;
    volumen = (Lado * Lado * altura) / 3;

    window.alert("el area de la piramide es" + area);
    window.alert("el volumen de la piramide es " + volumen);

  default:
    window.alert("figura no reconocida");

    break;
}
