#include <iostream>
using namespace std;
//Angel Omar Pardo Monreal
//12/5/2025
//Calcular el area de un triangulo
//Programa 3

int main() {
    float base, altura, area;

    cout << "Ingrese la base del triangulo: ";
    cin >> base;

    cout << "Ingrese la altura del triangulo: ";
    cin >> altura;

    area = (base * altura) / 2;

    cout << "El área del triangulo es: " << area << endl;

    return 0;
}

