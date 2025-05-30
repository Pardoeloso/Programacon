
#include <iostream>
#include <cmath>
#define M_PI 3.14159265358979323846 
//Angel Omar Pardo Monreal
//Segundo codigo
//08/05/2025
//Se debe calcular el area de un perimetro con clases de un circulo


using namespace std;

class Circulo {
private:
    double radio;

public:
    Circulo(double r) {
        radio = r;
    }

    double calcularArea() {
        return M_PI * pow(radio, 2);
    }

    double calcularPerimetro() {
        return 2 * M_PI * radio;
    }

    void mostrarResultados() {
        cout << "Radio del circulo: " << radio << " unidades" << endl;
        cout << "Area del circulo: " << calcularArea() << " unidades cuadradas" << endl;
        cout << "Perimetro del circulo: " << calcularPerimetro() << " unidades" << endl;
    }
};

int main() {
    double r;
    cout << "Ingresa el radio del circulo: ";
    cin >> r;

    Circulo miCirculo(r);
    miCirculo.mostrarResultados();

    return 0;
}

