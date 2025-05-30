#include <iostream>
#include <cmath> 
//Angel Omar Pardo Monreal
//Noveno codigo
//Calcular los intereses dados

using namespace std;

int main() {
    
    double depositoMensual = 1000.0;
    double tasaInteresMensual = 0.037; 
    int meses = 15 * 12; 

    
    double montoFinal = depositoMensual * ((pow(1 + tasaInteresMensual, meses) - 1) / tasaInteresMensual);

    
    cout << "Cantidad ahorrada despues de 15 anios: $" << montoFinal << endl;

    return 0;
}
