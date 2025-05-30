#include <iostream>
#include <cmath> 
//Angel Omar Pardo Monreal
//Tercer codigo
//08/05/2025
//Se debe calcular el area de un perimetro con clases de un circulo


using namespace std;


double calcularArea(double radio) {
    return M_PI * pow(radio, 2);
}


double calcularPerimetro(double radio) {
    return 2 * M_PI * radio;
}


int main() {
    double radio;

    cout << "Ingresa el radio del circulo: ";
    cin >> radio;

    double area = calcularArea(radio);
    double perimetro = calcularPerimetro(radio);

    cout << "Radio del circulo: " << radio << " unidades" << endl;
    cout << "Area del circulo: " << area << " unidades cuadradas" << endl;
    cout << "Perimetro del circulo: " << perimetro << " unidades" << endl;

    return 0;
}
\
