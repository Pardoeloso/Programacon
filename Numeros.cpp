#include <iostream>
#include <algorithm>
//Angel Omar Pardo Monreal
//Noveno Pragrama
// Capturar numeros y que se ordenen numeres ascendentemente 
using namespace std;

void metodo1() {
    cout << "\n=== METODO 1: SORT() ===" << endl;
    double numeros[10];
    
    cout << "Ingrese 10 numeros:" << endl;
    for(int i = 0; i < 10; i++) {
        cout << "Numero " << (i + 1) << ": ";
        cin >> numeros[i];
    }
    
    sort(numeros, numeros + 10);
    
    cout << "Numeros ordenados: ";
    for(int i = 0; i < 10; i++) {
        cout << numeros[i] << " ";
    }
    cout << endl;
}

int main() {
    metodo1();
    return 0;
}

