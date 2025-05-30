#include <iostream>
#include <stack>
//Angel Omar Pardo Monreal
//Sexto Codigo
//Hacer una secuencia con el diagrama dado
//20/05/2025
using namespace std;

string transicion(string estado, char simbolo) {
    if (estado == "S1") {
        if (simbolo == 'a') return "S2"; 
    } else if (estado == "S2") {
        if (simbolo == 'a') return "S2";
        if (simbolo == 'b') return "S1"; 
        if (simbolo == 'c') return "S4"; 
    } else if (estado == "S4") {
        if (simbolo == 'd') return "S3";
        if (simbolo == 'b') return "S4"; 
    } else if (estado == "S3") {
        if (simbolo == 'b') return "S4"; 
        if (simbolo == 'a') return "S1";
    }
    return "ERROR"; 
}

int main() {
    string cadena;
    string estado = "S1";
    stack<char> pila;

    cout << "Ingresa una cadena (solo a, b, c, d): ";
    cin >> cadena;

    for (int i = 0; i < cadena.length(); i++) {
        pila.push(cadena[i]);
    }


    while (!pila.empty()) {
        char simbolo = pila.top();
        pila.pop();

        string siguiente = transicion(estado, simbolo);
        if (siguiente == "ERROR") {
            cout << "No cumple con las condiciones " << estado << " con '" << simbolo << "'. Cadena NO aceptada.\n";
            return 0;
        }

        cout << estado << " --'" << simbolo << "'--> " << siguiente << endl;
        estado = siguiente;
    }

    cout << "\nEstado final: " << estado << endl;
    cout << "Cadena ACEPTADA" << endl;

    return 0;
}
