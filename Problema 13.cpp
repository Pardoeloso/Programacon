#include <iostream>
//Angel Omar Pardo Monreal
//Septimo programa 
// Calcular la cantidad ahorrada dada
// 26/05/2025

using namespace std;

int main() {
    double depositoMensual = 1000.0;
    double tasaInteres = 0.03; 
    int meses = 10 * 12;

   
    double montoFinal = depositoMensual * tasaInteres * meses / tasaInteres ;

    
    cout << "Cantidad ahorrada: $" << montoFinal << endl;

    return 0;
}
